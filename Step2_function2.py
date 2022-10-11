import urllib3
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

http = urllib3.PoolManager()

def login():
    try:
        token = (user, pwd)
        headers = {'Authorization': f'token {token}'}
        r = http.request('GET', url,  headers=headers, body=json.dumps(token).encode('UTF-8'))
        data = json.loads(r.data)

        #test1
        print(data)

        # Example 1: Print the name of the first group in the list
        print( 'First group = ', data['groups'][0]['name'] )

        # Example 2: Print the name of each group in the list
        group_list = data['groups']
        for group in group_list:
            print(group['name'])
        
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