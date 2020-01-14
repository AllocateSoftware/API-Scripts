import sys
sys.path.append("../Util")

import http.client
import json
import requests
from random import randint
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

#Load the timesheet payload
with open('timesheet.json') as json_file:  
    timesheet = json.load(json_file)

#Generate a random vacancyid
vacancyIdPrefix= "PW"
vacancyId =  "{}000{}".format(vacancyIdPrefix, randint(0, 10))

#Call the API
srvEndpoint = "{}/vacancies/{}/timesheet".format(API_ADDRESS, vacancyId)
print("URI: %s" %srvEndpoint)


r = requests.post(url = srvEndpoint, json = timesheet, headers = {"accept": "application/json", "AuthorizationToken" : bearer_auth}, verify=True)   
rsp = r.text

print("Response Code: %s" %r.status_code)
print("Response: %s" %rsp)


