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

def add_communication_to_case(event):
    try:
        attachment_data = {
            'ticket_id': event['id'],
            
            
        }

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
        #create_case()
        #describe_services()
        #describe_cases()
        
        cases = describe_cases()
        
        case1 = cases["cases"][0]
        case1status = case1["status"]
        print("Case 1 status is:", case1status)

        return {
            'statusCode': 200,
            'body': case1
        }

    except botocore.exceptions.ClientError as error:
        raise error