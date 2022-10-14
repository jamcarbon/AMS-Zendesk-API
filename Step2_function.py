import boto3
import botocore.exceptions
import json
import logging
import requests
from zenpy import Zenpy
#Documentation
#http://docs.facetoe.com.au/zenpy.html#usage
#source https://github.com/facetoe/zenpy


creds = {
    'email' : 'youremail',
    'token' : 'yourtoken',
    'subdomain': 'yoursubdomain'
}

def login():
    try:
        zenpy_client = Zenpy(**creds)

        ticket_data = {
            "ticket_status": ticket_json['ticket']["ticket_status"],
            "ticket_type": ticket_json['ticket']["ticket_type"],
            "ticket_priority": ticket_json['ticket']["ticket_priority"],
            "ticket_requester_name": ticket_json['ticket']["ticket_requester_name"],
            "ticket_service": ticket_json['ticket']["ticket_service"],
            "ticket_impact": ticket_json['ticket']["ticket_impact"],
            "created_at": ticket_json['ticket']["created_at"],
            "description": ticket_json['ticket']["description"],
            "ticket_id": ticket_json['ticket']["id"],
            "ticket_subject": ticket_json['ticket']["ticket_subject"],
            "updated_at": ticket_json['ticket']["updated_at"],
            "ticket_url": ticket_json['ticket']["ticket_url"],
            "public_comment": ticket_json['ticket']["public_comment"],
            "latest_public_comment": ticket_json['ticket']["latest_public_comment"],
            "ticket_tags": ticket_json['ticket']["ticket_tags"]
        }
        
    except botocore.exceptions.ClientError as error:
        raise error


def create_ticket():
    try:
        

    except botocore.exceptions.ClientError as error:
        raise error

def lambda_handler(event, context):
    try:
        print(event)

        return {
            'statusCode': 200,
            'body': json.dumps(           )
        }

    except botocore.exceptions.ClientError as error:
        raise error