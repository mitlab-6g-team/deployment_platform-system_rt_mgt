from django.urls import path
from main.apps.system_status_mgt.actors import TaskAllocationHandler, SystemMonitor

module_name = 'system_status_mgt'

urlpatterns = [
    path(f'{module_name}/TaskAllocationHandler/task_priority_manage', TaskAllocationHandler.task_priority_manage),
    path(f'{module_name}/TaskAllocationHandler/task_scehduling', TaskAllocationHandler.task_scehduling),
    path(f'{module_name}/SystemMonitor/get_positions', SystemMonitor.get_positions),
    path(f'{module_name}/SystemMonitor/get_system_load_ratio_to_node', SystemMonitor.get_system_load_ratio_to_node),
    path(f'{module_name}/SystemMonitor/get_system_load_ratio_to_limitation', SystemMonitor.get_system_load_ratio_to_limitation),
    path(f'{module_name}/SystemMonitor/get_inference_rt_info', SystemMonitor.get_inference_rt_info),
    path(f'{module_name}/SystemMonitor/get_inference_hosts', SystemMonitor.get_inference_hosts)
]
