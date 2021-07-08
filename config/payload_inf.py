
#Payload and headers for all 8 api tests
class Payload:
    headers = {'Content-Type': 'application/json'
               }

    payloadT001 = {}
    payloadT002 = {
        "description": {
            "raw": "This is the second test project"
        }
    }
    payloadT003 = {
        "_embedded": {
            "status": {
                "_type": "ProjectStatus",
                "id": "on_track",
                "name": "On track",
                "_links": {
                    "self": {
                        "href": "/api/v3/project_statuses/on_track",
                        "title": "On track"
                    }
                }
            }
        },
        "_type": "Project",
        "identifier": "newproject",
        "name": "NewProject",
        "active": 'true',
        "public": 'true',
        "description": {
            "format": "markdown",
            "raw": "This is the new test project",
            "html": "<p class=\"op-uc-p\">This is the first test project</p>"
        },
        "status": {
            "href": "/api/v3/project_statuses/on_track",
            "title": "On track"
        }
    }

    payloadT004 = {
    }

    payloadT005 = {
    }

    payloadT006 = {

        "lockVersion": 1,
        "description": {
            "raw": "test"
        }

    }

    payloadT007 = {

        "subject": "MyTask",
        "description": {
            "format": "markdown",
            "raw": "test",
            "html": "<p class=\"op-uc-p\">test</p>"
        },
        "scheduleManually": 'false',
        "type": {
            "href": "/api/v3/types/1",
            "title": "Task"
        },
        "project": {
            "href": "/api/v3/projects/14",
            "title": "TestProject1"
        }
    }

    payloadT008 = {
    }
