import boto3
import botocore.exceptions
import json
import os
import logging
import requests
from requests_oauthlib import OAuth1
import urllib3
import base64
from urllib.parse import urlencode

http = urllib3.PoolManager()
client = boto3.client('support')
clientdb = boto3.client('dynamodb')

DDB_TABLE = os.environ.get("DYNAMODB_TABLE")
if DDB_TABLE is None:
    raise ClientError("DYNAMODB_TABLE environment variable is undefined")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(DDB_TABLE)

language = "en"

user = 'david.montenegro@consegna.cloud' + '/token'
pwd = ""

full_token = ""
bearer_token = 'Bearer ' + full_token



def show_home():
    return template('home')
    
def make_request():
    if request.get_cookie('owat'):
        # Get user data
        access_token = request.get_cookie('owat')
        bearer_token = 'Bearer ' + access_token
        header = {'Authorization': bearer_token}
        url = 'https://consegna.zendesk.com/api/v2/tickets/41894'
        r = requests.get(url, headers=header)
        if r.status_code != 200:
            error_msg = 'Failed to get data with error {}'.format(r.status_code)
            return template('error', error_msg=error_msg)
        else:
            rjson = response.json()
            return rjson
    else:
        # Kick off authorization flow
        parameters = {
            'response_type': 'code',
            'redirect_uri': 'http://localhost:8080/handle_user_decision',
            'client_id': 'AMS_Integration',
            'scope': 'read write'}
        url = 'https://your_subdomain.zendesk.com/oauth/authorizations/new?' + urlencode(parameters)
        redirect(url)

def get_ticket():
    try:
        #url = 'https://consegna.zendesk.com/api/v2/tickets/39322'
        url = 'https://consegna.zendesk.com/api/v2/tickets/41894'
      
        headers = {'Accept': "application/json",
            'Content-Type': "application/json", 
            'Authorization': full_token}
        
        #r = http.request('GET', url, auth=(user, pwd), headers=headers)
        response = requests.get(url, headers=headers)
        rjson = response.json()
        
        #print(type(rjson))
        #print(rjson)
        return rjson
    
    except botocore.exceptions.ClientError as error:
        raise error
        
        
def get_clientID():
    try:
        url = 'https://consegna.zendesk.com/api/v2/oauth/clients.json'
      
        headers = {'Content-Type': "application/json"}
        
        #r = http.request('GET', url, auth=(user, pwd), headers=headers)
        response = requests.get(url, auth=(user, pwd), headers=headers)
        rjson = response.json()
        
        #print(type(rjson))
        #print(rjson)
        return rjson
    
    except botocore.exceptions.ClientError as error:
        raise error
        

def create_access_token():
    try:
        url = 'https://consegna.zendesk.com/api/v2/oauth/tokens.json'
      
        headers = {'Content-Type': "application/json"}
        payload = '{"token": {"client_id": "13030325183897", "scopes": ["read", "write"]}}'
        
        #r = http.request('GET', url, auth=(user, pwd), headers=headers)
        response = requests.post(url, data=payload, auth=(user, pwd), headers=headers)
        rjson = response.json()
        
        #print(type(rjson))
        #print(rjson)
        return rjson
    
    except botocore.exceptions.ClientError as error:
        raise error
        

def lambda_handler(event, context):
    try:
        #print(event)
        
        

        #ticket_info = get_ticket(event)

        #main
        #eventDetailType = event["detail-type"]
        #eventName = event["detail"]["eventName"]
        
        #f eventDetailType == "AWS API Call via CloudTrail":
        #    if eventName == "CreateCase":
        #        ticket_data = describe_cases_create(event)
        #        ticket_info = create_ticket(ticket_data)
        #        ticket_json = ticket_info.json()
        #        print(ticket_json)
        #    elif eventName == "AddCommunicationToCase":
        #        ticket_data = describe_cases_update(event)
        #        ticket_info = update_ticket(ticket_data)
        #        ticket_json = ticket_info.json()
        #        print(ticket_json)

        #else:
        #    return "There was no event from CLoudTrail"
        
        g = get_ticket()
        #g = make_request()
        #g = get_clientID()
        #g = create_access_token()
        print(g)
        print(type(g))
        #j = json.loads(g)
        js = json.dumps(g, indent=2)
        #print(js)
        print(type(js))
        
        return g

    except botocore.exceptions.ClientError as error:
        raise error
