import requests


class HttpClient:
    def __init__(self):
        self.__session = requests.session()

    def get(self, path, **kwargs):
        return self.__request(path, "GET", **kwargs)

    def post(self, path, data=None, json=None, **kwargs):
        return self.__request(path, "POST", data, json, **kwargs)

    def __request(self, url, method, data=None, json=None, **kwargs):
        resp = None
        if method == "GET":
            resp = self.__session.get(url, **kwargs)
        elif method == "POST":
            resp = self.__session.post(url, data, json, **kwargs)
        return resp
