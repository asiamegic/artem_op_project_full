
from config.config import TestData
from config.payload_inf import Payload
from infra.work_packages_client import WorkPackagesClient

#Test 006 - API - Update Work Package
def test_T006():

    work_packages_client = WorkPackagesClient()
    response = work_packages_client.get_work_packages(TestData.id_work_packages, Payload.payloadT006)
    resp_body = response.json()

    print(resp_body)
    des = resp_body['description']['raw']

    assert des == "test"
    assert response.status_code == 200
