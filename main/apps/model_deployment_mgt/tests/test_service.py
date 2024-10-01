from django.test import TestCase
from unittest.mock import patch
from django.test import TestCase, Client
from main.utils.env_loader import default_env
from main.apps.model_deployment_mgt.services.modules.inference_host_tools import check_image_exists_in_harbor
import json
from main.utils.api_caller import call_api
import shutil, os


    
# Create your tests here.
class TestModelMgtHandlerService(TestCase):
    """_summary_
    
    unittest for services in ModelMgtHandler

    Args:
        TestCase (_type_): _description_
    """
    
    def setUp(self):
        """
        unittest request initialize
        """
        self.client = Client()
        
    def test_check_image_exists_in_harbor(self):
        """
        test send the position information and token, 
        then issue certificate as response
        """
        check_image_exists_in_harbor('inference_host', '4e39b436-cce0-499d-af71-9fab79910fbe', 'aaaabbbb-4459-461c-8b8e-b3b154f8e5d7')
        
    def test_remove_inference_host_directory(self):
        """
        test send the position information and token, 
        then issue certificate as response
        """
        inference_host_path = f'''{os.path.expanduser('~')}/inference_host'''
        shutil.rmtree(f'{inference_host_path}/4e39b436-cce0-499d-af71-9fab79910fbe')
        
    def test_position_remove(self):
        """
        test send the position information and token, 
        then issue certificate as response
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"application_source_mgt/SourceCertificateHandler/certificate_issuing")

        # build the payload and header
        payload_dict  = {
            'application_token' : '12134',
            'inference_client_name' : '56456',
            'position_uid': '2222'
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
        test send the position information and token, 
        then issue certificate as response
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"application_source_mgt/SourceCertificateHandler/certificate_issuing")

        # build the payload and header
        payload_dict  = {
            'application_token' : '12134',
            'inference_client_name' : '56456',
            'position_uid': '2222'
            }
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
    def test_remove_inference_host_image_in_harbor(self):
        """
        test remove image in harbor
        """
       
        from main.apps.model_deployment_mgt.services.modules.inference_host_tools import remove_inference_host_image_in_harbor

        # unit test begin
        response = remove_inference_host_image_in_harbor("32df6185-4567-41d5-b9ee-4896e2babb52")