# Serialization: Convert object in Python to bytes & back
# Formats: JSON, YAML, CSV, TOML, Protocol buffers, XML, ...

# Types: JSON <-> Python
# null <-> None
# string <-> str
# true/false <-> True/False (bool)
# number <-> int, float (complex, ...)
# array <-> list
# object <-> dict
# MIA:
# str (2025-05-07T18:57:14), int (seconds since epoch) <-> datetime
# str (base64 encoding) <-> bytes
# comments

# json module API
# loads, dumps: str/bytes
# load, dump: file like objects
# load: JSON -> Python
# dump: Python -> JSON
import json
from urllib.request import urlopen, Request
from http import HTTPStatus
from pprint import pprint
# import requests

event = {
    'action': 'start',
    'image': 'ubuntu',
    'count': 1,
    'tags': ['qa', 'us-1']
}  # fmt: off

data = json.dumps(event)
print(data)
# data['image']  # error: data is a str
print('data type:', type(data))

event2 = json.loads(data)
print(event2['image'])

"""
$ curl -i https://api.github.com/users/tebeka
HTTP/2 200  <<- Status line
date: Wed, 07 May 2025 16:17:14 GMT <<- Header
content-type: application/json; charset=utf-8
...
content-length: 1396

{ <<- content/body
  "login": "tebeka",
  "id": 87697,
  "node_id": "MDQ6VXNlcjg3Njk3",
  "avatar_url": "https://avatars.githubusercontent.com/u/87697?v=4",
  ...
}
"""

# Will raise is status >= 400
# Will follow redirect
with urlopen('https://api.github.com/users/tebeka') as fp:
    print('status:', fp.status)
    # print(HTTPStatus.OK)

    print('ctype:', fp.headers['Content-Type'])
    # print('data:', fp.read(256))
    reply = json.load(fp)
print(reply['login'])


# Exercise: Write a function github_info(login)
# And return a tuple with the user name (name), and number
# of public repos (public_repos)
def github_info(login):
    # TODO: URL escape login
    url = f'https://api.github.com/users/{login}'
    with urlopen(url) as fp:
        reply = json.load(fp)

    name = reply['name']
    num_repos = reply['public_repos']
    return (name, num_repos)


print(github_info('tebeka'))

# REST API: HTTP + JSON

# Acroynms:
# URL: Uniform Resource Locator
# HTTP: HyperText Transfer Protocol
# JSON: JavaScript Object Notation
# API: Application Programmable Interface
# REST: REpresentational State Transfer
# verbs: GET, POST, PUT, DELETE

"""Client request

POST /events HTTP/1.1
Host: httpbin.org
...

{
    "type": "access",
    "login": "elliot",
    "uri": "file:///etc/passwd"
}
"""

body = {
    'type': 'access',
    'login': 'elliot',
    'uri': 'file:///etc/password',
}

req = Request(
    url='https://httpbin.org/post',
    method='POST',
    headers={
        'Authorization': 'Bearer s3cr3t',
        'Content-Type': 'application/json'
    },
    # data must by bytes, json.dumps returns str
    data=json.dumps(body).encode(),
)  # fmt: off

with urlopen(req) as fp:
    reply = json.load(fp)

pprint(reply)
