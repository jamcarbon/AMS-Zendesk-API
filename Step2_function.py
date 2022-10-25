import boto3
import botocore.exceptions
import json
import logging
import requests
import urllib3
#from zenpy import Zenpy
#Documentation
#http://docs.facetoe.com.au/zenpy.html#usage
#source https://github.com/facetoe/zenpy

http = urllib3.PoolManager()


def create_ticket():
    try:
        url = 'https://consegna.zendesk.com/api/v2/tickets.json'
        user = 'test@email.com' + '/token'
        pwd = 'tokengeneratedfromzendesk'
        
        subject = 'THIS IS A TEST TICKET'
        body = 'PLEASE IGNORE'
        service = 'AWS Generic Tasks'
        impact = 'No Impact'
        Resolution_Code = 'Permanently Resolved'

        headers = {'content-type': 'application/json'}
        #data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'service': service, 'impact': impact, 'Resolution_Code': Resolution_Code}}
        data = {'ticket': {'subject': subject, 'comment': {'body': body}}}
        payload = json.dumps(data)
        #r = http.request('POST', url, auth=(user, pwd), headers=headers, data=payload)
        response = requests.post(url, data=payload, auth=(user, pwd), headers=headers)
        rjson = response.json()
        
        print(type(rjson))
        print(rjson)
        return response
    
    except botocore.exceptions.ClientError as error:
        raise error

def update_ticket():
    try:
        id = '103'
        body = 'Thanks for choosing Acme Jet Motors.'
        url = 'https://consegna.zendesk.com/api/v2/tickets.json' + id + '.json'
        user = 'david.montenegro@consegna.cloud' + '/token'
        pwd = 'hDO9hxHyC4maXaisRQr3ShKZQxblGqBl69j4OGGL'
        
        subject = 'THIS IS A TEST TICKET'
        body = 'PLEASE IGNORE'
        service = 'AWS Generic Tasks'
        impact = 'No Impact'
        Resolution_Code = 'Permanently Resolved'

        headers = {'content-type': 'application/json'}
        data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'service': service, 'impact': impact, 'Resolution_Code': Resolution_Code}}
        payload = json.dumps(data)
        r = http.request('POST', url,  data=payload, auth=(user, pwd), headers=headers)
        data = json.loads(r.data)
        
        
        print(data)
        return data
    
    except botocore.exceptions.ClientError as error:
        raise error

def get_ticket():
    try:
        id = '40879'
        body = 'Thanks for choosing Acme Jet Motors.'
        url = 'https://consegna.zendesk.com/api/v2/tickets/41172'
        user = 'david.montenegro@consegna.cloud' + '/token'
        pwd = 'hDO9hxHyC4maXaisRQr3ShKZQxblGqBl69j4OGGL'
        
        
        headers = {'content-type': 'application/json'}
        
        #r = http.request('GET', url, auth=(user, pwd), headers=headers)
        response = requests.get(url, auth=(user, pwd), headers=headers)
        rjson = response.json()
        
        print(type(rjson))
        print(rjson)
        return response
    
    except botocore.exceptions.ClientError as error:
        raise error
        
def get_brands():
    try:
        body = 'Thanks for choosing Acme Jet Motors.'
        url = 'https://consegna.zendesk.com/api/v2/brands'
        user = 'david.montenegro@consegna.cloud' + '/token'
        pwd = 'hDO9hxHyC4maXaisRQr3ShKZQxblGqBl69j4OGGL'
        
        
        headers = {'content-type': 'application/json'}
        
        response = requests.get(url, auth=(user, pwd), headers=headers)
        #data = json.loads(response)
        print(type(response))
        rjson = response.json()
        
        #parsed = json.loads(rjson)
        #print(json.dumps(rjson, indent=4))
        print(type(rjson))
        print(rjson)
        return response
    
    except botocore.exceptions.ClientError as error:
        raise error
        
def get_ticketfields():
    try:
        url = 'https://consegna.zendesk.com/api/v2/ticket_fields'
        user = 'david.montenegro@consegna.cloud' + '/token'
        pwd = 'hDO9hxHyC4maXaisRQr3ShKZQxblGqBl69j4OGGL'
        
        
        headers = {'content-type': 'application/json'}
        
        response = requests.get(url, auth=(user, pwd), headers=headers)
        #data = json.loads(response)
        print(type(response))
        rjson = response.json()
        
        #parsed = json.loads(rjson)
        #print(json.dumps(rjson, indent=4))
        print(type(rjson))
        print(rjson)
        return response
    
    except botocore.exceptions.ClientError as error:
        raise error

def lambda_handler(event, context):
    try:
        #print(event)

        ticket_info = get_ticket()
        
        reply = "Zendesk ticket created"
        ticket_json = ticket_info.json()
        
        print(ticket_json)
        print(type(ticket_json))

        return ticket_json

    except botocore.exceptions.ClientError as error:
        raise error