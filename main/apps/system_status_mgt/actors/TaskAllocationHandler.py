"""
TaskAllocationHandler
"""
import json
from django.http import HttpResponse
from main.utils.logger import log_trigger, log_writer


@log_trigger("INFO")
def task_priority_manage(request):
    """
    task_priority_manage 
    """
    log_writer('INFO', task_priority_manage, (request,),
               message="Task priority_manage")
    return HttpResponse('task_priority_manage')


@log_trigger("INFO")
def task_scehduling(request):
    """
    task_scehduling 
    """
    log_writer('INFO', task_scehduling, (request,), message="Task scehduling")
    return HttpResponse('task_scehduling')
