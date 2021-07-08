The project of testing api and ui on service OpenProject installed on a local computer based by docker virtualization.



The code is written in Python. Testing is done using the PyTest library.

Description of the task is in the file - technical_task.pdf.



    Description of the functionality of the files

API_Testing(postman).json - contains 8 api tests for the postman program
------------------
config(dir)
    config - contains all variables including authorization
    payload_inf- request body for api tests
    locator- all locations of web elements for ui tests
------------------
infra(dir)
    http_client- sending requests through API test libraries
    projects_client- receiving variable project numbers and request body from api test
    work_packages_client- the same for work packages
------------------
Pages(dir)
    files- division into objects of the testing window of the ui test
------------------
pytestApi(dir)
    files- all api tests
------------------
pytestUi(dir)
    conftest- creating a web driver
    test_Ui_CreateProject- run ui test 09 number
    test_Ui_CreateTask- run ui test 10 number


------------------
created by Artem Rafikov
asia.megic@gmail.com
------------------

