from main.apps.model_deployment_mgt.services.modules.inference_host_tools import inference_host_initialize, remove_inference_host_image_in_harbor
from main.apps.model_deployment_mgt.services.modules.inference_node_connector import (
    check_inferece_rt_mgt_exist,
    deploy_inference_rt_mgt,
    delete_inference_rt_mgt,
    check_is_container_running)
from main.utils.api_caller import call_api


def position_init(data):

    # update position status
    payload = {
        "position_uid": data['position_uid'],
        "position_deploy_status": "Deploying"
    }

    call_api('agent', "PositionManager", "update", payload)

    # status report
    deploy_inference_rt_mgt(data['position_uid'], data['external_port'])

    while not check_is_container_running(data['external_port']):
        pass

    # build image process
    inference_host_initialize(
        data['parent_model_uid'], data['model_uid'], data['position_uid'])

    # deploy one inference host
    payload = {
        "application_uid": data['application_uid'],
        "position_uid": data['position_uid'],
        "external_port": data['external_port'],
        "model_uid": data['model_uid'],
        "file_extension": data['file_extension'],
        "num_of_deployment": "1",
        "resource_requirements": data['resource_requirements']
    }
    deploy_inference_host(payload)


def deploy_inference_host(data):

    payload = {
        "application_uid": data['application_uid'],
        "position_uid": data['position_uid'],
        "model_uid": data['model_uid'],
        "file_extension": data['file_extension'],
        "num_of_deployment": data['num_of_deployment'],
        "external_port": data['external_port']
    }

    call_api("inference_rsc_mgt", "InferenceRscMgtHandler", "inference_unit_deploy",
             payload, data['external_port'])

    payload = {
        "position_uid": data['position_uid'],
        "position_deploy_status": "InService"
    }

    call_api('agent', "PositionManager", "update", payload)


def remove_inference_host(data):

    payload = {
        "position_uid": data['position_uid'],
        "num_of_deployment": data['num_of_deployment'],
        "resource_requirements": {
            "cpu_requests": "default",
            "cpu_limits": "default",
            "memory_requests": "default",
            "memory_limits": "default"
        }
    }

    call_api("inference_rsc_mgt", "InferenceRscMgtHandler", "inference_unit_remove",
             payload, data['external_port'])


def remove_position(data):

    for uid in data['position_uid']:

        payload = {
            "application_uid": data['application_uid'],
            "position_uid": uid,
            "num_of_deployment": '0',
            "external_port": data['external_port'][data['position_uid'].index(uid)]
        }

        # remove inference hosts and service in k8s
        remove_inference_host(payload)

        # remove master container
        delete_inference_rt_mgt(uid)

        # remove inference host image
        remove_inference_host_image_in_harbor(uid)


def update_position(data):

    # rebuild new image process
    inference_host_initialize(data['model_uid'], data['position_uid'])

    call_api("inference_rsc_mgt", "InferenceRscMgtHandler", "inference_unit_update",
             data, data['external_port'])


def check_position_created(position_uid):

    return check_inferece_rt_mgt_exist(position_uid)
