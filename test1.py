import boto3
import botocore.exceptions
import json

client = boto3.client('support')

def add_communication_to_case(ticket_data):
    try:
        #ticket_data
        response = client.add_communication_to_case(
            caseId='string',
            communicationBody='string',
            ccEmailAddresses=[
                'string',
            ],
            attachmentSetId='string'
        )
    except botocore.exceptions.ClientError as error:
        raise error

def lambda_handler(event, context):
    try:        
        ticket_body = event['body']
        
        ticket_json = json.loads(ticket_body)

        ticket_id= ticket_json['ticket']["id"]
        
        i = {
                "reply": "The ticket has been updated sucesfully.",
                "ticket_id": ticket_id
            }
        
        reply = "The ticket", ticket_id, "has been updated sucesfully."
        reply1 = "The ticket has been updated sucesfully."
        
        print(ticket_id)
        #print("all public comments", public_comment)
        #print("latest comment", latest_comment)
        #print("ticket_data", ticket_data)

        #dd_communication_to_case(ticket_data)
        
        return {
            'statusCode': 200,
            'body': reply1
        }
    
    except botocore.exceptions.ClientError as error:
        raise error

