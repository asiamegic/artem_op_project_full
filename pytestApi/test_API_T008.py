
from config.config import TestData
from config.payload_inf import Payload
from infra.work_packages_client import WorkPackagesClient

#Test 008 - API - Delete Work Package
def test_T008():


    work_packages_client = WorkPackagesClient()
    response = work_packages_client.delete_work_packages(TestData.id_work_packages, Payload.payloadT008)



    assert response.status_code == 204

    response = work_packages_client.delete(TestData.id_work_packages, Payload.payloadT008)
    assert response.status_code == 404
