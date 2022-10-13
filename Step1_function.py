import boto3
import botocore.exceptions
import json

client = boto3.client('support')

language = "en"
ncsubject = "TEST CASE-Please ignore"
servicecode = "service-ams-operations-service-request"
ncseverutycode = "low"
nccategorycode = "other"
ncbody = "TEST PLEASE IGNORE"

def create_case ():
    try:
        response = client.create_case(
            caseIdList=[
                '10912303471',
            ],
            subject=ncsubject,
            serviceCode=servicecode,
            severityCode=ncseverutycode,
            categoryCode=nccategorycode,
            communicationBody=ncbody,
            ccEmailAddresses=[
                'string',
            ],
            language=language,
            attachmentSetId='string'
        )
        print(response)

    except botocore.exceptions.ClientError as error:
        raise error

def describe_services():
    try:
        response = client.describe_services(
            serviceCodeList=[
                'service-ams-operations-service-request',
            ],
            language=language
        )
        return(response)

    except botocore.exceptions.ClientError as error:
        raise error


def describe_cases():
    try:
        response1 = client.describe_cases(
            includeResolvedCases=False,
            maxResults=10,
            language=language,
            includeCommunications=False
        )
    
        return(response1)

    except botocore.exceptions.ClientError as error:
        raise error


def add_communication_to_case(ticket_data):
    try:
        aws_ticket_id = ticket_data["ticket_subject"][-11:]
        AMSticketbody = ticket_data["latest_public_comment"]
        response = client.add_communication_to_case(
            caseId=aws_ticket_id,
            communicationBody=AMSticketbody 
        )
        print(response)
        print("Successfully updated AMS ticket #:", aws_ticket_id)
        return aws_ticket_id
        
    except botocore.exceptions.ClientError as error:
        raise error

def lambda_handler(event, context):
    try:        
        ticket_body = event['body']
        
        ticket_json = json.loads(ticket_body)

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
        
        ticket_status = ticket_json['ticket']["ticket_status"]
        ticket_type = ticket_json['ticket']["ticket_type"]
        ticket_priority = ticket_json['ticket']["ticket_priority"]
        ticket_requester_name = ticket_json['ticket']["ticket_requester_name"]
        ticket_service = ticket_json['ticket']["ticket_service"]
        ticket_impact = ticket_json['ticket']["ticket_impact"]
        created_at = ticket_json['ticket']["created_at"]
        description = ticket_json['ticket']["description"]
        ticket_id= ticket_json['ticket']["id"]
        ticket_subject = ticket_json['ticket']["ticket_subject"]
        updated_at = ticket_json['ticket']["updated_at"]
        ticket_url = ticket_json['ticket']["ticket_url"]
        public_comment = ticket_json['ticket']["public_comment"]
        latest_public_comment = ticket_json['ticket']["latest_public_comment"]
        ticket_tags = ticket_json['ticket']["ticket_tags"]

        
        
        i = {
                "reply": "The ticket has been updated sucesfully.",
                "ticket_id": ticket_id
            }
        
        reply = "The ticket", ticket_id, "has been updated sucesfully."
        reply1 = "The ticket has been updated sucesfully."
        
        print(ticket_id)
        print("all public comments", public_comment)
        print("latest comment", latest_comment)
        print("ticket_data", ticket_data)

        #add_communication_to_case(ticket_data)
        
        return {
            'statusCode': 200,
            'body': reply1
        }
    
    except botocore.exceptions.ClientError as error:
        raise error

