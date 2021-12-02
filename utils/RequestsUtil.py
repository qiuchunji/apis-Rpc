import requests
from utils.LogUtil import my_log


def requests_get(url, headers):
    res = requests.get(url, headers=headers)
    code = res.status_code
    try:
        body = res.json()
    except Exception as e:
        body = res.text
    res_data = dict()
    res_data["code"] = code
    res_data["body"] = body
    return res_data


def requests_post(url, data, json, headers):
    res = requests.post(url, data, json, headers=headers)
    code = res.status_code
    try:
        body = res.json()
    except Exception as e:
        body = res.text
    res_data = dict()
    res_data["code"] = code
    res_data["body"] = body
    return res_data


class Request:
    # 定义公共方法
    def __init__(self):
        self.log = my_log("Requests")

    def requests_api(self, url, params=None, json=None, headers=None, cookies=None, method="get"):
        if method == "get":
            self.log.info("Method: get request")
            res = requests.get(url, json=json, params=params, headers=headers, cookies=cookies)
            self.log.info("Params =====>> %s", str(params))
            self.log.info("Response Status Code =====>> %s", str(res.status_code))
            self.log.info("Response =====>> %s", str(res.text))
        elif method == "post":
            self.log.info("Method: post request")
            res = requests.post(url, json=json, data=params, headers=headers, cookies=cookies)
            self.log.info("Params =====>> %s", str(params))
            self.log.info("Response Status Code =====>> %s", str(res.status_code))
            self.log.info("Response =====>> %s", str(res.text))
        code = res.status_code
        try:
            body = res.json()
        except Exception as e:
            body = res.text
        res_data = dict()
        res_data["code"] = code
        res_data["body"] = body
        return res_data

    # 重构get/post方法
    def get(self, url, **kwargs):
        return self.requests_api(url, method="get", **kwargs)

    def post(self, url, **kwargs):
        return self.requests_api(url, method="post", **kwargs)

