
from config.payload_inf import Payload
from config.config import TestData
from infra.projects_client import ProjectsClient


#Test 002 - API - get Project
def test_T001():

    project_client = ProjectsClient()
    response = project_client.get_project(TestData.id_project, Payload.payloadT001)

    resp_body = resp.json()
    name = resp_body['name']
    new_description = resp_body['description']['raw']

    print(new_description)
    # assert
    assert response.status_code == 200
    assert name == "TestProject1"
    assert new_description == "This is the first test project"

test_T001()



