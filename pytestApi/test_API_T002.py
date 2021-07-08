
from config.config import TestData
from config.payload_inf import Payload
from infra.projects_client import ProjectsClient

#Test 002 - API - Update Project
def test_T002():



    project_client = ProjectsClient()
    response = project_client.patch_project(TestData.id_project, Payload.payloadT002)
    resp_body = response.json()
    print(resp_body)
    name = resp_body['name']
    new_description = resp_body['description']['raw']

    print(new_description)

    assert response.status_code == 200
    assert name == "TestProject1"
    assert new_description == "This is the second test project"
