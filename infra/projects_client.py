import json

from infra.http_client import HttpClient
from config.config import TestData
from requests.auth import HTTPBasicAuth


class ProjectsClient(HttpClient):
    def __init__(self):
        self.base_url = TestData.host_url_api
        self.http_client = HttpClient(TestData.host_url_api)
        self.headers = TestData.header
        self.auth = HTTPBasicAuth(TestData.Auth_name, TestData.Auth_Key)


    def create_project(self, project_id: str, body):

        command = {
            'headers': self.headers,
            'route': f'/projects/{project_id}',
            'auth': self.auth,
            'body': body
        }


        return self.http_client.post(command)

    def get_project(self, project_id: str, body):
        command = {
            'headers': self.headers,
            'route': f'/projects/{project_id}',
            'auth': self.auth,
            'body': body
        }
        return self.http_client.get(command)

    def patch_project(self, project_id: str, body):
        command = {
            'headers': self.headers,
            'route': f'/projects/{project_id}',
            'auth': self.auth,
            'body': body
        }
        return self.http_client.patch(command)

    def delete_project(self, project_id: str, body):
        command = {
            'headers': self.headers,
            'route': f'/projects/{project_id}',
            'auth': self.auth,
            'body': body
        }
        return self.http_client.delete(command)

