#!/usr/bin/env python3
from client import API
import json

link = "https://jsonplaceholder.typicode.com/posts"
api = API(link=link)

dict1 = {"userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}

def test_match_statuscode():
    assert api.status_code() == 200

def test_headers():
    trueHeader = 'application/json; charset=utf-8'
    assert api.getHeaders() == trueHeader

def Test_json():
    jsonapi = json.loads(api.getText())
    assert api.getJson() == jsonapi

def test_match_json():
    assert api.getJson()[0] == dict1