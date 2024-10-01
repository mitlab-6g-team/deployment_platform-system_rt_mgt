"""
ModelMgtHandler
"""
import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger, log_writer
from main.apps.model_deployment_mgt.services.inference_backend import position_init, deploy_inference_host, remove_inference_host, remove_position, update_position, check_position_created
from threading import Thread    
    
@require_POST
@log_trigger("INFO")
def position_initialize(request):
    """
    position_initialize 
    """
    data = json.loads(request.body.decode('utf-8'))
    
    # create master container
    if(check_position_created(data['position_uid'])):
        
        return HttpResponse(
                json.dumps({
                    'status': 'error', 
                    'message' : 'position_uid has already existed', 
                    'position_uid' : data['position_uid']
                })
            )
    
    thread = Thread(target=position_init, args=(data, ))
    thread.start()
    
    return HttpResponse(
                json.dumps({
                    "status" : "success", 
                    "message": "get deploy_initialize_process command",
                    "application_uid" : data["application_uid"], 
                    "model_uid" : data["model_uid"] 
                })
            )

        
@require_POST
@log_trigger("INFO")
def model_deploy(request):
    """
    model_deploy 
    """
    data = json.loads(request.body.decode('utf-8'))
    
    if(not check_position_created(data['position_uid'])) :
        
        return HttpResponse(
                json.dumps({
                    'status': "error", 
                    'message' : "position_uid hasn't been created", 
                    'position_uid' : data['position_uid']
                })
            )
        
    thread = Thread(target=deploy_inference_host, args=(data, ))
    thread.start()
    
    return HttpResponse(
                json.dumps({
                    "status" : "success", 
                    "message": "get inference_host_deployment command",
                    "num_of_deployment" : data['num_of_deployment'],
                    "application_uid" : data["application_uid"]
                })
            )

@require_POST
@log_trigger("INFO")
def position_remove(request):
    """
    position_remove 
    """
    data = json.loads(request.body.decode('utf-8'))
    
    for position_uid in data['position_uid']:
        if(not check_position_created(position_uid)) :
            
            return HttpResponse(
                    json.dumps({
                        'status': "error", 
                        'message' : "position_uid hasn't been created", 
                        'position_uid' : data['position_uid']
                    })
                )
            
    thread = Thread(target=remove_position, args=(data, ))
    thread.start()
    
    return HttpResponse(
            json.dumps({
                "status" : "success", 
                "message": "get position_removal command",
                "application_uid" : data["application_uid"],
                "position_uid": data["position_uid"]
            })
        )

@require_POST
@log_trigger("INFO")
def model_remove(request):
    """
    model_remove 
    """
    data = json.loads(request.body.decode('utf-8'))
    
    if(not check_position_created(data['position_uid'])):
        return HttpResponse(
                json.dumps({
                    'status': "error", 
                    'message' : "position_uid hasn't been created", 
                    'position_uid' : data['position_uid']
                })
            )
    
    thread = Thread(target=remove_inference_host, args=(data, ))
    thread.start()
    
    return HttpResponse(
            json.dumps({
                "status" : "success", 
                "message": "get inference_host_removal command",
                "num_of_deployment" : data['num_of_deployment'],
                "application_uid" : data["application_uid"],
                "position_uid" : data['position_uid']
            })
        )
        
        

@require_POST
@log_trigger("INFO")
def model_update(request):
    """
    model_update 
    """
    data = json.loads(request.body.decode('utf-8'))
    
    if(not check_position_created(data['position_uid'])):
        return HttpResponse(
                json.dumps({
                    'status': "error", 
                    'message' : "position_uid hasn't been created", 
                    'position_uid' : data['position_uid']
                })
            )
    
    thread = Thread(target=update_position, args=(data, ))
    thread.start()
    
    return HttpResponse(
            json.dumps({
                "status" : "success", 
                "message": "get model_update command",
                "application_uid" : data["application_uid"],
                "position_uid" : data['position_uid']
            })
        )