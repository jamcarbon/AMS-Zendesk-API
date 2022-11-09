import boto3
import botocore.exceptions
import json
import os

client = boto3.client('support')

language = "en"

def add_communication_to_case(ams_caseID, ticket_data):
    try:
        AMSticketbody = ticket_data["latest_public_comment"]
        response = client.add_communication_to_case(
            caseId=ams_caseID,
            communicationBody=AMSticketbody 
        )
        print(response)
        print("Successfully updated AMS ticket #:", ams_caseID)
        return ams_caseID
        
    except botocore.exceptions.ClientError as error:
        raise error

def lambda_handler(event, context):
    try:        
        ticket_body = event['body']
        ticket_json = json.loads(ticket_body)

        #ticket_json = event["body"]

        ticket_data = {
            "ticket_status": ticket_json['ticket']["ticket_status"],
            "ticket_type": ticket_json['ticket']["ticket_type"],
            "ticket_priority": ticket_json['ticket']["ticket_priority"],
            "ticket_requester_name": ticket_json['ticket']["ticket_requester_name"],
            "ticket_external_id": ticket_json['ticket']["ticket_external_id"],
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
        
        reply = "The ticket", ticket_data["ticket_id"], "has been updated sucesfully."
        reply1 = "The ticket has been updated sucesfully."
        
        print("ticket_data", ticket_data)

        ams_caseID = ticket_data["ticket_external_id"]

        add_communication_to_case(ams_caseID, ticket_data)
        
        reply2 = "The AMS ticket #", ams_caseID,  "has been updated sucesfully."

        return {
            'statusCode': 200,
            'body': reply2
        }
    
    except botocore.exceptions.ClientError as error:
        raise error