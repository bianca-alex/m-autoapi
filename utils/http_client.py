# -*- coding: utf-8 -*-
import requests
import sys
from utils.logger import logger
import json

class HttpClient:
    def __init__(self, base_url=None):
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None, cookies=None):
        res = requests.get(str(self.base_url) + "/" + str(endpoint), params=params, headers=headers, cookies=cookies)
        return self.handleRes(res)

    def post(self, endpoint, data=None, headers=None, cookies=None):
        res = requests.post(str(self.base_url) + "/" + str(endpoint), json=data, headers=headers, cookies=cookies)
        return self.handleRes(res)

    # excel导入执行测试用例
    def excelTemple(self, test_case):
        no = test_case['用例编号']
        url = test_case['url']
        method = test_case['请求方法']
        headers = json.loads(test_case['请求头'])
        cookies = test_case['cookies']
        data = test_case['请求体']
        logger.info(headers)
        if method == 'POST':
            return self.post(url, data, headers, cookies)
        elif method == 'GET':
            return self.get(url, data, headers, cookies)
        else:
            logger.error("不支持的请求方法")
            sys.exit()

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