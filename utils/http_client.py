# coding=utf-8
import requests
from utils.logger import logger

class HttpClient:
    def __init__(self, base_url=None):
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None, cookies=None):
        res = requests.get(str(self.base_url) + "/" + str(endpoint), params=params, headers=headers, cookies=cookies)
        return self.handleRes(res)

    def post(self, endpoint, data=None, headers=None, cookies=None):
        res = requests.post(str(self.base_url) + "/" + str(endpoint), json=data, headers=headers, cookies=cookies)
        return self.handleRes(res)

    def handleRes(self, res):
        code = res.status_code
        cookies = res.cookies.get_dict()
        myDict = dict()
        try:
            body = res.json()
        except:
            body = res.text

        myDict['code'] = code
        myDict['body'] = body
        myDict['cookies'] = cookies
        myDict['headers'] = res.headers
        myDict['time']    = res.elapsed.total_seconds() * 1000 # ms
        
        return myDict

if __name__ == "__main__":
    pass