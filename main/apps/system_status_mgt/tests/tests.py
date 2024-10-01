from django.test import TestCase
from unittest.mock import patch
from django.test import TestCase, Client
from main.utils.env_loader import default_env
import json

# Create your tests here.
class TestSystemMonitor(TestCase):
    """_summary_
    
    unittest for SystemMonitor

    Args:
        TestCase (_type_): _description_
    """
    
    def setUp(self):
        """
        unittest request initialize
        """
        self.client = Client()
        
    def test_get_positions(self):
        """
        test to get all the position in specific inference node
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"system_status_mgt/SystemMonitor/get_positions")

        # build the payload and header
        payload_dict  = {
            "external_port": "30304",
            "position_uid": "hello-world"
        }
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
        print(response.content.decode('utf-8'))
        
    def test_get_system_load_ratio_to_node(self):
        """
        test to get the CPU, Memory usage ratio of each inference host in one position to a inference node resources
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"system_status_mgt/SystemMonitor/get_system_load_ratio_to_node")

        # build the payload and header
        payload_dict  = {
            "external_port": "32001",
            "position_uid": "4e39b436-cce0-499d-af71-9fab79910fbe"
        }
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
        print(response.content.decode('utf-8'))
    
    def test_get_system_load_ratio_to_limitation(self):
        """
        test to get the CPU, Memory usage ratio of each inference host in one position to a initial limitation
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"system_status_mgt/SystemMonitor/get_system_load_ratio_to_limitation")

        # build the payload and header
        payload_dict  = {
            "external_port": "30304",
            "position_uid": "hello-world"
        }
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
        print(response.content.decode('utf-8'))
    
    def test_get_inference_rt_info(self):
        """
        test to get the CPU, Memory usage about inference_rt (master container)
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"system_status_mgt/SystemMonitor/get_inference_rt_info")

        # build the payload and header
        payload_dict  = {
            "position_uid": "kong"
        }
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
        print(response.content.decode('utf-8'))
        
    def test_get_inference_hosts(self):
        """
        test to get the number of inference hosts in specific position
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"system_status_mgt/SystemMonitor/get_inference_hosts")

        # build the payload and header
        payload_dict  = {
            "external_port": "30304",
            "position_uid": "hello-world"
        }
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
        print(response.content.decode('utf-8'))