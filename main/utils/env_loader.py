"""
load env
"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv(".env.common")
load_dotenv()


@dataclass
class Default:
    """
        load default env
    """
    LOGS_FOLDER_PATH: str
    DJANGO_SETTINGS_MODULE: str
    DEBUG: str
    ALLOWED_HOSTS: str
    API_ROOT: str
    API_VERSION: str
    HOST_PASSWORD: str
    


default_env = Default(
    LOGS_FOLDER_PATH=os.environ.get('LOGS_FOLDER_PATH'),
    DJANGO_SETTINGS_MODULE=os.environ.get('DJANGO_SETTINGS_MODULE'),
    DEBUG=os.environ.get('DEBUG'),
    ALLOWED_HOSTS=os.environ.get('ALLOWED_HOSTS'),
    API_ROOT=os.environ.get('API_ROOT'),
    API_VERSION=os.environ.get('API_VERSION'),
    HOST_PASSWORD=os.environ.get('HOST_PASSWORD'),
)

@dataclass
class Customized:
    """
        load customized env
    """
    HTTPS_HARBOR_HOST: str
    HTTPS_HARBOR_USER: str
    HTTPS_HARBOR_PASSWORD: str
    AGENT_HOST_IP: str
    AGENT_PORT: str
    AGENT_VERSION: str
    AGENT_NAME: str
    
    INFERENCE_RSC_MGT_HOST_IP: str
    INFERENCE_RSC_MGT_VERSION: str
    INFERENCE_RSC_MGT_NAME: str
    
    INFERENCE_RSC_MONITORING_HOST_IP: str
    INFERENCE_RSC_MONITORING_VERSION: str
    INFERENCE_RSC_MONITORING_NAME: str
    
    POSITION1_DOCKER_PORT: str
    
customized_env = Customized(
    HTTPS_HARBOR_HOST=os.environ.get('HTTPS_HARBOR_HOST'),
    HTTPS_HARBOR_USER=os.environ.get('HTTPS_HARBOR_USER'),
    HTTPS_HARBOR_PASSWORD=os.environ.get('HTTPS_HARBOR_PASSWORD'),
    AGENT_HOST_IP=os.environ.get('AGENT_HOST_IP'),
    AGENT_PORT=os.environ.get('AGENT_PORT'),
    AGENT_VERSION=os.environ.get('AGENT_VERSION'),
    AGENT_NAME=os.environ.get('AGENT_NAME'),
    
    INFERENCE_RSC_MGT_HOST_IP=os.environ.get('INFERENCE_RSC_MGT_HOST_IP'),
    INFERENCE_RSC_MGT_VERSION=os.environ.get('INFERENCE_RSC_MGT_VERSION'),
    INFERENCE_RSC_MGT_NAME=os.environ.get('INFERENCE_RSC_MGT_NAME'),
    
    INFERENCE_RSC_MONITORING_HOST_IP=os.environ.get('INFERENCE_TASK_MGT_HOST_IP'),
    INFERENCE_RSC_MONITORING_VERSION=os.environ.get('INFERENCE_RT_MGT_VERSION'),
    INFERENCE_RSC_MONITORING_NAME=os.environ.get('INFERENCE_RSC_MONITORING_NAME'),
    
    POSITION1_DOCKER_PORT=os.environ.get('POSITION1_DOCKER_PORT')
)