import requests


class BaseAPI():

    def __init__(self):
        self.base_url = "https://www.baidu.com"

    def test_api(self, url, payload):
        api_url = self.base_url + url
        response = requests.post(url=api_url, data=payload)
        return response
