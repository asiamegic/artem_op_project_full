
from config.config import TestData
from config.payload_inf import Payload
from infra.work_packages_client import WorkPackagesClient

#Test 005 - API - Get Work Package by ID
def test_T005():


    work_packages_client = WorkPackagesClient()
    response = work_packages_client.create_work_packages(TestData.id_work_packages, Payload.payloadT005)
    resp_body = response.json()

    print(resp_body)
    task = resp_body['_embedded']['type']['name']
    subject = resp_body['subject']
    print(task)

    assert subject == "My Task 1"
    assert task == "Task"
    assert response.status_code == 200
