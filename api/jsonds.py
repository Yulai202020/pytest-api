#!/usr/bin/env python3
from apiclient import client

jsonplaceholder = client.API("https://jsonplaceholder.typicode.com/posts")
request = jsonplaceholder.status_code()

print(request)