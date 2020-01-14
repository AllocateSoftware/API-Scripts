import sys
sys.path.append("../Util")

import http.client
import json
import requests
import testUtil

CLIENT_ID = "Vm4XEKesciuMuDSg3pGjlhTwx5bqdsX9"
CLIENT_SECRET = input("Enter the CLIENT_SECRET? ")
AUDIENCE = "http://healthsuite.allocatesoftware.com/api/v1/workerapi"


API_ADDRESS = "https://interop-apigateway.allocate-dev.co.uk/workerapi"

#Get access token for the worker API
tokenQuery = testUtil.getTokenQuery(clientId = CLIENT_ID, clientSecret = CLIENT_SECRET, audience = AUDIENCE)
token = testUtil.getToken(tokenQuery)

bearer_auth = token["access_token"]
print("Token: %s" %bearer_auth)

allocate_worker_id = "9e6f9c02-2010-11ea-a585-069fc0af5368"

#Call the API
srvEndpoint = "{}/workers/{}".format(API_ADDRESS, allocate_worker_id)
print("URI: %s" %srvEndpoint)

r = requests.get(url = srvEndpoint, headers = {"accept": "application/json", "AuthorizationToken" : bearer_auth}, verify=True)   
rsp = r.text

print("Response Code: %s" %r.status_code)
print("Response: %s" %rsp)


