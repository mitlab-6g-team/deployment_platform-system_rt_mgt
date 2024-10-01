from main.utils.env_loader import customized_env
from main.utils.api_caller import cross_system_caller, call_api
import docker
from docker import errors

inference_node_ip = customized_env.INFERENCE_RSC_MGT_HOST_IP
client = docker.DockerClient(base_url=f'tcp://{inference_node_ip}:{customized_env.POSITION1_DOCKER_PORT}')

def get_position_list():
    
    try: 
        resp = client.containers.list()
        return [getattr(i, 'name') for i in resp]
        
    except errors.NotFound:
        return {'status': 'error', 'msg': 'container NotFound'}
    
    except errors.APIError:
        return {'status': 'error', 'msg': 'APIError'}
    
def get_stats_of_inference_rt(position_uid):
   
    container = client.containers.get(container_id=position_uid)
    resp = container.stats(stream=False)
    
    return resp

def get_inference_hosts_number(position_uid, external_port):
    
    payload={'position_uid': position_uid}
    resp = call_api(
        "inference_rsc_monitoring",
        "RscMonitor",
        "position_deployment_number",
        payload,
        external_port
    )
    
    return resp.content.decode('utf-8')

def get_system_load_in_node(position_uid, external_port):
    
    payload={'position_uid': position_uid}
    resp = call_api(
        "inference_rsc_monitoring",
        "RscMonitor",
        "position_usage_in_node",
        payload,
        external_port
    )
   
    return resp.content.decode('utf-8')

def get_system_load_in_limitation(position_uid, external_port):
    
    payload={ 'position_uid': position_uid}
    resp = call_api(
        "inference_rsc_monitoring",
        "RscMonitor",
        "position_usage_in_limitation",
        payload,
        external_port
    )
    
    return resp.content.decode('utf-8')