import urllib3
import boto3
import botocore.exceptions
import json

from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket, User
from zenpy.lib.api_objects import Comment
#Documentation
#http://docs.facetoe.com.au/zenpy.html#usage
#source https://github.com/facetoe/zenpy


creds = {
    'email' : 'youremail',
    'token' : 'yourtoken',
    'subdomain': 'yoursubdomain'
}

http = urllib3.PoolManager()
zenpy_client = Zenpy(**creds)

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


def create_ticket(ticket_data):
    try:
        zenpy_client.tickets.create(
            Ticket(description='Some description',
                requester=User(name='bob', email='bob@example.com'))
        )

    except botocore.exceptions.ClientError as error:
        raise error

def update_ticket(ticket_data):
    try:
        ticket = zenpy_client.tickets(id=some_ticket_id)
        ticket.comment = Comment(body="Important private comment", public=False)
        zenpy_client.tickets.update(ticket)

    except botocore.exceptions.ClientError as error:
        raise error

def lambda_handler(event, context):
    try:
        print(event)

        ticket_body = event['body']
        ticket_body = event
        
        ticket_json = json.loads(ticket_body)

        ticket_data = {
            "ticket_uid": ticket_json["id"],
            "ticket_details": ticket_json['detail-type'],
            "ticket_source": ticket_json["source"],
            "ticket_account": ticket_json["account"],
            "ticket_time": ticket_json["time"],
            "ticket_region": ticket_json["region"],
            #"ticket_requester_name": ticket_json['ticket']["ticket_requester_name"],
            "ticket_case_id": ticket_json["case-id"],
            "ticket_id": ticket_json['detail']["display-id"],
            "ticket_communicationid": ticket_json["communication-id"],
            "ticket_event_name": ticket_json["event-name"],
            "ticket_origin": ticket_json["origin"]

            #"ticket_priority": ticket_json['ticket']["ticket_priority"],
            #"ticket_requester_name": ticket_json['ticket']["ticket_requester_name"],
            #"updated_at": ticket_json['ticket']["updated_at"],
            #"public_comment": ticket_json['ticket']["public_comment"],
            #"latest_public_comment": ticket_json['ticket']["latest_public_comment"],
        }

        return {
            'statusCode': 200,
            'body': json.dumps(           )
        }

    except botocore.exceptions.ClientError as error:
        raise error