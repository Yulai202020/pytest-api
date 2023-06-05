import requests
from requests.auth import HTTPBasicAuth
from requests import Response

def connect(link:str, user:str, password:str) -> Response:
    auth = HTTPBasicAuth(user, password)
    try:
        req = requests.get(link, auth=auth)
        return req
    except requests.exceptions.SSLError:
        raise Exception("Cannot connect to site (incorrect adress).")
    except requests.exceptions.ConnectionError:
        raise Exception("No internet.")

class API:

    def __init__(self, link:str, user:str = None, password:str = None) -> None:
        self.link = link
        self.user = user
        self.password = password
        self.req = connect(self.link, self.user, self.password)

    def getRespone(self) -> Response:
        return self.req

    def getText(self) -> str:
        return self.req.text

    def getJson(self) -> list:
        return self.req.json()

    def getHeaders(self) -> str:
        return self.req.headers['content-type']

    def status_code(self) -> int:
        return self.req.status_code
    
    def getEncoding(self) -> str:
        return self.req.encoding
