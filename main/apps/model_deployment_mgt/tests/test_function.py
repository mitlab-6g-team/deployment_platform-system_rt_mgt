from django.test import TestCase
from unittest.mock import patch
from django.test import TestCase, Client
from main.utils.env_loader import default_env
import json

# Create your tests here.
class TestModelMgtHandler(TestCase):
    """_summary_
    
    unittest for ModelMgtHandler

    Args:
        TestCase (_type_): _description_
    """
    
    def setUp(self):
        """
        unittest request initialize
        """
        self.client = Client()
        
    def test_position_initialize(self):
        """
        test to do position initialize
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"model_deployment_mgt/ModelMgtHandler/position_initialize")

        # build the payload and header
        payload_dict  = {
            "application_uid": "45df6fb4-79ca-41d5-b9ee-4896e2babb52", 
            "position_uid": "32df6185-4567-41d5-b9ee-4896e2babb52",
            "external_port": "32001",
            "parent_model_uid": "6462e2d8-3527-8008-bdc2-180df358a589",
            "model_uid": "f5e8d7c6-b9a8-4321-9876-543210fedcba",
            "file_extension": ".h5",
            "resource_requirements": {
                "cpu_requests": "default",
                "cpu_limits": "default",
                "memory_requests": "default",
                "memory_limits": "default"
            }
        }
        
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        print('###########')
        print(response.content)
        print('###########')
        
    def test_model_deploy(self):
        """
        test to deploy a number of inference hosts
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"model_deployment_mgt/ModelMgtHandler/model_deploy")

        # build the payload and header
        payload_dict  = {
            "application_uid": "45df6fb4-79ca-41d5-b9ee-4896e2babb52",
            "position_uid": "32df6185-4567-41d5-b9ee-4896e2babb52",
            "model_uid": "f5e8d7c6-b9a8-4321-9876-543210fedcba",
            "external_port": "32001",
            "num_of_deployment" : "1",
            "resource_requirements": {
                "cpu_requests": "default",
                "cpu_limits": "default",
                "memory_requests": "default",
                "memory_limits": "default" 
            }
        }
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
    def test_position_remove(self):
        """
        test to remove single or multiple position at once
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"model_deployment_mgt/ModelMgtHandler/position_remove")

        # build the payload and header
        payload_dict  = {
            "application_uid": "45df6fb4-79ca-41d5-b9ee-4896e2babb52",
            "external_port": ["32001"],
            "position_uid": ["32df6185-4567-41d5-b9ee-4896e2babb52"]
        }
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
    def test_model_remove(self):
        """
        test to remove a number of inference_host in speific position
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"model_deployment_mgt/ModelMgtHandler/model_remove")

        # build the payload and header
        payload_dict  = {
            "application_uid": "45df6fb4-79ca-41d5-b9ee-4896e2babb52",
            "external_port": "32001",
            "position_uid": "4e39b436-cce0-499d-af71-9fab79910fbe",
            "num_of_deployment" : "1"
        }
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
        
    def test_model_update(self):
        """
        test to update all the inference_hosts in speific position
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"model_deployment_mgt/ModelMgtHandler/model_update")

        # build the payload and header
        payload_dict  = {
            "application_uid": "45df6fb4-79ca-41d5-b9ee-4896e2babb52", 
            "position_uid": "4e39b436-cce0-499d-af71-9fab79910fbe",
            "model_uid": "bbbbdddd-4459-461c-8b8e-b3b154f8e5d7",
            "external_port": "32001",
            "resource_requirements": {
                "cpu_requests": "default",
                "cpu_limits": "default",
                "memory_requests": "default",
                "memory_limits": "default" 
            }
        }
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
    def test_test(self):
        from main.utils.api_caller import call_api
        payload = {
            "position_uid": "test",
            "position_deploy_status": "OutOfService"
        }

        call_api('agent', "PositionManager", "update", payload)