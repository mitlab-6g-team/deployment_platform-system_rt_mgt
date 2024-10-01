
from main.utils.env_loader import customized_env
from main.utils.api_caller import call_api
import docker, os
from docker import errors


position_ip = customized_env.INFERENCE_RSC_MGT_HOST_IP
docker_port = customized_env.POSITION1_DOCKER_PORT
client = docker.DockerClient(
    base_url=f'tcp://{position_ip}:{docker_port}')

def check_inferece_rt_mgt_exist(position_uid):
    
    try: 
        client.containers.get(container_id=position_uid)
        return True
        
    except errors.NotFound:
        return False
    
    except errors.APIError:
        print('msg: APIError')
        return False
    
    
    
def deploy_inference_rt_mgt(position_uid, external_port):
    
    harbor_host = customized_env.HTTPS_HARBOR_HOST
    home_dir = f'{os.path.expanduser("~")}'
    
    try: 
        client.containers.run(
            f'{harbor_host}/position/master_container:latest',  
            detach=True, 
            ports={'30304/tcp': external_port}, 
            name=position_uid, 
            volumes=[f'{home_dir}/.kube/config:/root/.kube/config']
        )
        
    except errors.ContainerError:
        return {'status': 'error', 'msg': 'ContainerError'}
    
    except errors.ImageNotFound:
        return {'status': 'error', 'msg': 'ImageNotFound'}
    
    except errors.APIError:
        return {'status': 'error', 'msg': 'APIError'}

def delete_inference_rt_mgt(position_uid):
    
    try: 
        container = client.containers.get(position_uid)
        container.stop()
        container.remove()
        
    except errors.NotFound:
        return {'status': 'error', 'msg': 'ContainerNotFound'}
    
    except errors.APIError:
        return {'status': 'error', 'msg': 'APIError'}
    

def check_is_container_running(external_port):
    
    try:
        resp = call_api(
                'inference_rsc_mgt',
                'InferenceRscMgtHandler',
                'executing_test',
                {},
                external_port
            )
        
        return resp['status'] == 'success'
        
    except:
        return False
