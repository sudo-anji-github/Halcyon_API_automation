# api_endpoints = {}
request_headers = {}
request_bodies = {}
import requests

import pdb

# pdb.set_trace()

url = "https://uat-api.halcyonportal.com/halcyonhub/v1/consumer/fi/authenticate"
request_headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
request_headers['Content-Type'] = "application/json"
request_headers['Ocp-Apim-Subscription-Key'] = "3881a8a1ae654a9890fab37d96a55266"
request_body = {"userName": "jimmcgowan", "password": "Abcd@1234", "fiName": "family first funding"}

# Method for to generate Auth token for Database
def auth_token_gen():
    response = requests.post(url=url, json=request_body, headers=request_headers)
    return "Bearer " + response.json()['responseData']['token']

request_headers['Authorization'] = auth_token_gen()
