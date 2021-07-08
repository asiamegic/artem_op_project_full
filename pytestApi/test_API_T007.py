
from config.config import TestData
from config.payload_inf import Payload
from infra.work_packages_client import WorkPackagesClient

#Test 007 - API - Create Work Package
def test_T007():


    work_packages_client = WorkPackagesClient()
    response = work_packages_client.patch_work_packages(TestData.id_work_packages, Payload.payloadT007)
    resp_body = response.json()

    print(resp_body)
    sub = resp_body['subject']

    assert sub == "MyTask"
    assert response.status_code == 201
