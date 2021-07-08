
from config.config import TestData
from config.payload_inf import Payload
from infra.projects_client import ProjectsClient

#Test 004 - API - Delete Project
def test_T004():


    project_client = ProjectsClient()
    response = project_client.delete_project(TestData.id_project, Payload.payloadT004)


    assert response.status_code == 204
    project_client = ProjectsClient()
    response1 = project_client.delete_project(TestData.id_project, Payload.payloadT004)
    assert response1.status_code == 404
