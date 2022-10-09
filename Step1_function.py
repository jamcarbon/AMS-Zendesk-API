import boto3
import botocore.exceptions
import json
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