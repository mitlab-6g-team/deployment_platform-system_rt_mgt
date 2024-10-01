import os, shutil, base64
import requests, docker
from docker import errors
from main.utils.env_loader import customized_env

client = docker.from_env()
file_system_path = f'''{os.path.expanduser('~')}/inference_file_system'''
inference_host_path = f'''{os.path.expanduser('~')}/inference_host'''

def build_inference_host(parent_model_uid, model_uid, position_uid):
    print(f'''build_inference_host --- parent_model_uid: {parent_model_uid}, model_uid: {model_uid}, position_uid: {position_uid}''')
    
    tag_name = f'''{customized_env.HTTPS_HARBOR_HOST}/inference_host/{position_uid}:{model_uid}'''
    model_file_path = os.path.join(file_system_path, parent_model_uid)
    target_path = os.path.join(inference_host_path, position_uid)
    shutil.copytree(f'''{model_file_path}/template''', target_path, dirs_exist_ok=True)

    model_file = None
    for file in os.listdir(model_file_path):
        if file.startswith(model_uid) and os.path.isfile(os.path.join(model_file_path, file)):
            model_file = file
            break

    if not model_file:
        return {'status': 'error', 'msg': f'''Model file for {model_uid} not found'''}

    source_model_path = os.path.join(model_file_path, model_file)
    _, file_extension = os.path.splitext(model_file)
    target_model_path = os.path.join(target_path, 'model', f'model{file_extension}')

    shutil.copyfile(source_model_path, target_model_path)

    try:
        client.images.build(path=target_path, tag=tag_name, rm=True)
        
    except errors.BuildError:
        _update_position_status(position_uid, "OutOfService")
        return {'status': 'error', 'msg': 'BuildError'}
    
    except errors.APIError:
        _update_position_status(position_uid, "OutOfService")
        return {'status': 'error', 'msg': 'APIError'}

    host_image_name = _push_image(tag_name)
    
    _remove_local_image(tag_name) #remove the local image immediately
    
    return host_image_name

def check_image_exists_in_harbor(project_name, repository_name, model_uid):
    print(f'''check_image_exists_in_harbor --- repository_name: {repository_name}''')
    api_url = f'''http://{customized_env.HTTPS_HARBOR_HOST}/api/v2.0/projects/{project_name}/repositories'''
    credentials = _get_basic_auth_credentials(customized_env.HTTPS_HARBOR_USER, customized_env.HTTPS_HARBOR_PASSWORD)
    headers = {'Authorization': f'Basic {credentials}'}

    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    repositories = response.json()
    for repo in repositories:
        if repo['name'] == f'''{project_name}/{repository_name}''':
            
            tags = _get_tags_in_repository(project_name, repository_name)
            for tag in tags :
                if tag == model_uid: return True
                    
            return False
    return False

def inference_host_initialize(parent_model_uid, model_uid, position_uid):
    print(f'''inference_host_initialize --- model_uid: {model_uid}, position_uid: {position_uid}''')
    host_image_name = None
    inference_host_exists = check_image_exists_in_harbor('inference_host', position_uid, model_uid)
    try:
        if not inference_host_exists:
            host_image_name = build_inference_host(parent_model_uid, model_uid, position_uid)
            msg = 'Inference host image built successfully.'
            
            # remove the env image and the directory in inference_host directory
            _remove_inference_host_directory(position_uid, model_uid)
        else:
            host_image_name = f'''{customized_env.HTTPS_HARBOR_HOST}/inference_host/{position_uid}:{model_uid}'''
            msg = 'Inference host image already exists'
        
        print({'status': 'success', 'msg': msg, 'host_image_name': host_image_name})
        return {'status': 'success', 'msg': msg, 'host_image_name': host_image_name}
    except Exception as e:
        _update_position_status(position_uid, "OutOfService")
        return {'status': 'error', 'msg': str(e)}


def get_cotainer_list():
    image_list = client.images.list()
    output = []
    
    for i in image_list:
        output.append(getattr(i, 'tags')[0])
    
    return output


def remove_inference_host_image_in_harbor(position_uid):
    api_url = f"http://{customized_env.HTTPS_HARBOR_HOST}/api/v2.0/projects/inference_host/repositories/{position_uid}"
    credentials = _get_basic_auth_credentials(customized_env.HTTPS_HARBOR_USER, customized_env.HTTPS_HARBOR_PASSWORD)
    headers = {'Authorization': f'Basic {credentials}'}
   
    response = requests.delete(api_url, headers=headers)
    response.raise_for_status()
    
    return response


# private function
def _push_image(tag_name):
    
    try:
        client.api.push(repository=tag_name)
        return {'status': 'success', 'msg': 'finish pushing'}
    
    except errors.APIError:
        return {'status': 'error', 'msg': 'APIError'}
    
    
def _remove_local_image(image_name):

    try:
        client.images.remove(image = image_name)
        return {'status': 'success', 'msg': 'finish removing'}
    
    except:
        return {'status': 'error', 'msg': 'unknown error'}


def _remove_inference_host_directory(position_uid, model_uid):
    shutil.rmtree(f'{inference_host_path}/{position_uid}')
    

def _get_basic_auth_credentials(username: str, password: str) -> str:
    credentials = f"{username}:{password}".encode('utf-8')
    return base64.b64encode(credentials).decode('utf-8')

def _get_tags_in_repository(project_name, repository_name):
    
    api_url = f"http://{customized_env.HTTPS_HARBOR_HOST}/api/v2.0/projects/{project_name}/repositories/{repository_name}/artifacts"
    credentials = _get_basic_auth_credentials(customized_env.HTTPS_HARBOR_USER, customized_env.HTTPS_HARBOR_PASSWORD)
    headers = {'Authorization': f'Basic {credentials}'}

    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    repositories = response.json()
    tags = [tag['tags'][0]['name'] for tag in repositories if(tag['tags'])]

    return tags

def _update_position_status(position_uid, status):
    from main.utils.api_caller import call_api
    # update position status
    payload = {
        "position_uid": position_uid,
        "position_deploy_status": status
    }

    call_api('agent', "PositionManager", "update", payload)