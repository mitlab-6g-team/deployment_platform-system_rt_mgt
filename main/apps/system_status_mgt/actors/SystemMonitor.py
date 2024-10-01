"""
SystemMonitor
"""
import json
from django.http import HttpResponse
from main.utils.logger import log_trigger, log_writer
from main.apps.system_status_mgt.services.positions_info import (
    get_position_list, 
    get_stats_of_inference_rt, 
    get_inference_hosts_number, 
    get_system_load_in_node, 
    get_system_load_in_limitation)

    
#only one inference node for now
@log_trigger("INFO")
def get_positions(request):
    """
    get_positions 
    
    get the positions list in specific inference node
    """
    return HttpResponse(json.dumps({"position_uid": get_position_list()}))


@log_trigger("INFO")
def get_system_load_ratio_to_node(request):
    """
    get_system_load_ratio_to_node 
    
    get the CPU, Memory usage ratio of each inference host in one position to a inference node resources
    """
    data = json.loads(request.body.decode('utf-8'))
    
    return HttpResponse(get_system_load_in_node(data['position_uid'], data['external_port']))


@log_trigger("INFO")
def get_system_load_ratio_to_limitation(request):
    """
    get_system_load_ratio_to_limitation 
    
    get the CPU, Memory usage ratio of each inference host in one position to a initial limitation
    """
    
    data = json.loads(request.body.decode('utf-8'))
    
    return HttpResponse(get_system_load_in_limitation(data['position_uid'], data['external_port']))

@log_trigger("INFO")
def get_inference_rt_info(request):
    """
    get_inference_rt_info 
    
    get the CPU, Memory usage about inference_rt (master container)
    """
    data = json.loads(request.body.decode('utf-8'))
    
    return HttpResponse(json.dumps(get_stats_of_inference_rt(data['position_uid'])))

@log_trigger("INFO")
def get_inference_hosts(request):
    """
    get_inference_hosts 
    
    get the number of inference hosts in specific position
    """
    data = json.loads(request.body.decode('utf-8'))
    
    return HttpResponse(get_inference_hosts_number(data['position_uid'], data['external_port']))