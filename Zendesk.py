import urllib3
from AMS import lambda_handler
import boto3
import botocore.exceptions
import json

url = 'https://your_subdomain.zendesk.com/api/v2/groups.json'
user = 'your_email_address' + '/token'
pwd = 'your_password'

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

def lambda_handler(event, context):
    try:
        print(event)

        return {
            'statusCode': 200,
            'body': json.dumps(           )
        }

    except botocore.exceptions.ClientError as error:
        raise error