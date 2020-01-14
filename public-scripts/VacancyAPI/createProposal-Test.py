import sys
sys.path.append("../Util")

import http.client
import json
import requests
import testUtil

CLIENT_ID = "Vm4XEKesciuMuDSg3pGjlhTwx5bqdsX9"
CLIENT_SECRET = input("Enter the CLIENT_SECRET? ")
AUDIENCE = "http://healthsuite.allocatesoftware.com/api/v1/vacancyapi"


API_ADDRESS = "https://interop-apigateway.allocate-dev.co.uk/vacancyapi"

#Get access token for the vacancy API
tokenQuery = testUtil.getTokenQuery(clientId = CLIENT_ID, clientSecret = CLIENT_SECRET, audience = AUDIENCE)
token = testUtil.getToken(tokenQuery)

bearer_auth = token["access_token"]
print("Token: %s" %bearer_auth)

#Load the proposed worker payload
with open('proposed-worker.json') as json_file:  
    proposedworker = json.load(json_file)

#VacancyId must exist (ie, from vacancy published event)
vacancyId =  "cdfc2b38-1a99-11ea-9b96-fa6bc8f7cf0b"

#Call the API
srvEndpoint = "{}/vacancies/{}/proposals".format(API_ADDRESS, vacancyId)
print("URI: %s" %srvEndpoint)


r = requests.post(url = srvEndpoint, json = proposedworker, headers = {"accept": "application/json", "AuthorizationToken" : bearer_auth}, verify=False)   
rsp = r.text

print("Response Code: %s" %r.status_code)
print("Response: %s" %rsp)


