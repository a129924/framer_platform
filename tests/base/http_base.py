import requests


class HttpClient:
    def __init__(self):
        self.__session = requests.session()

    def get(self, url, **kwargs):
        return self.__request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.__request(url, "POST", data, json, **kwargs)

    def __request(self, url, method, data=None, json=None, **kwargs):
        resp = None
        if method == "GET":
            resp = self.__session.get(url, **kwargs)
        elif method == "POST":
            resp = self.__session.post(url, data, json, **kwargs)
        return resp
