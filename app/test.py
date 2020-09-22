import requests
from requests.auth import HTTPDigestAuth
url = "http://127.0.0.1:5000/"

payload = {}

response = requests.request("GET", url, data = payload, auth=HTTPDigestAuth("vcu", "rams"))

print(response.text.encode('utf8'))
