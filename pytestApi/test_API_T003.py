
from config.config import TestData
from config.payload_inf import Payload
from infra.projects_client import ProjectsClient

#Test 003 - API - Create NEW Projec
def test_T003():


    project_client = ProjectsClient()
    response = project_client.create_project(TestData.id_project, Payload.payloadT003)
    resp_body = response.json()

    print(resp_body)
    name1 = resp_body['name']
    id = resp_body['id']
    print(id)
    identifier = resp_body['identifier']
    assert response.status_code == 201
    assert name1 == "NewProject"
    assert identifier == "newproject"
