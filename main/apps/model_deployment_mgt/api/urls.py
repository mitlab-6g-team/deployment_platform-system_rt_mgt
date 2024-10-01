from django.urls import path
from main.apps.model_deployment_mgt.actors import ModelMgtHandler

module_name = 'model_deployment_mgt'

urlpatterns = [
    # path(f'{module_name}/ModelMgtHandler/test', ModelMgtHandler.service_test),
    path(f'{module_name}/ModelMgtHandler/position_initialize', ModelMgtHandler.position_initialize),
    path(f'{module_name}/ModelMgtHandler/position_remove', ModelMgtHandler.position_remove),
    path(f'{module_name}/ModelMgtHandler/model_deploy', ModelMgtHandler.model_deploy),
    path(f'{module_name}/ModelMgtHandler/model_remove', ModelMgtHandler.model_remove),
    path(f'{module_name}/ModelMgtHandler/model_update', ModelMgtHandler.model_update)
]
