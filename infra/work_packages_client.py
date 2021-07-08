import json

from infra.http_client import HttpClient
from config.config import TestData
from requests.auth import HTTPBasicAuth


class WorkPackagesClient:
    def __init__(self):
        self.base_url = TestData.host_url_api
        self.http_client = HttpClient(TestData.host_url_api)
        self.headers = TestData.header
        self.auth = HTTPBasicAuth(TestData.Auth_name, TestData.Auth_Key)


    def create_work_packages(self, id_work_packages: str, body):
        # setup
        command = {
            'headers': self.headers,
            'route': f'/work_packages/{id_work_packages}',
            'auth': self.auth,
            'body': body
        }

        # get
        return self.http_client.post(command)

    def get_work_packages(self, id_work_packages: str, body):
        command = {
            'headers': self.headers,
            'route': f'/work_packages/{id_work_packages}',
            'auth': self.auth,
            'body': body
        }
        return self.http_client.get(command)

    def patch_work_packages(self, id_work_packages: str, body):
        command = {
            'headers': self.headers,
            'route': f'/work_packages/{id_work_packages}',
            'auth': self.auth,
            'body': body
        }
        return self.http_client.path(command)

    def delete_work_packages(self, id_work_packages: str, body):
        command = {
            'headers': self.headers,
            'route': f'/work_packages/{id_work_packages}',
            'auth': self.auth,
            'body': body
        }
        return self.http_client.delete(command)
