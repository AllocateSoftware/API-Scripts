import http.client
import json
import requests
from random import randint
import re
import uuid
from faker import Faker

AUTH0_DOMAIN = "allocatesoftware.eu.auth0.com"

def getTokenQuery(clientId, clientSecret, audience):
    data = {"client_id" : clientId, 
    "client_secret" : clientSecret,
    "audience" : audience ,
    "grant_type" : "client_credentials"}
    return json.dumps(data)

def getToken(tokenQuery, auth0Domain = AUTH0_DOMAIN):
    payload = tokenQuery

    conn = http.client.HTTPSConnection(auth0Domain)
    headers = { 'content-type': "application/json" }
    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def getRandomisedWorker(worker):    
    wid = str(uuid.uuid1())[:8]
    #random id
    worker["ids"][0]["id"] = wid
    fake = Faker()    
    worker["identification"]["forenames"] = [fake.first_name(), fake.first_name()]
    worker["identification"]["surname"] = fake.last_name()
    worker["identification"]["dateOfBirth"] = str(fake.date_of_birth())
    return worker

def poisonToken(token):
    return token + "Bad"    