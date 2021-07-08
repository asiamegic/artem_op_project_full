import requests



class HttpClient:
    def __init__(self, base_url: str):
        self.base_url = base_url


    def get(self, http_command):
        # get
        url = f'{self.base_url}{http_command["route"]}'
        headers = http_command['headers']
        auth = http_command['auth']

        return requests.get(url, auth=auth, headers=headers)

    def post(self, http_command):
        # post
        url = f'{self.base_url}{http_command["route"]}'
        headers = http_command['headers']
        auth = http_command['auth']
        body = http_command['body']

        return requests.post(url, auth=auth, headers=headers , json=body)

    def patch(self, http_command):
        # patch
        url = f'{self.base_url}{http_command["route"]}'
        headers = http_command['headers']
        auth = http_command['auth']
        body = http_command['body']

        return requests.patch(url, auth=auth, headers=headers , json=body)

    def delete(self, http_command):
        # delete
        url = f'{self.base_url}{http_command["route"]}'
        headers = http_command['headers']
        auth = http_command['auth']

        return requests.delete(url, auth=auth, headers=headers)
