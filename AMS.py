import boto3
import botocore.exceptions
import json

client = boto3.client('support')


def create_case ():
    try:
        response = client.create_case(
            subject='string',
            serviceCode='string',
            severityCode='string',
            categoryCode='string',
            communicationBody='string',
            ccEmailAddresses=[
                'string',
            ],
            language='string',
            issueType='string',
            attachmentSetId='string'
        )
        print(response)

    except botocore.exceptions.ClientError as error:
        raise error

def describe_services():
    try:
        response = client.describe_services(
            serviceCodeList=[
                'sentinel-service-request',
            ],
            language='en'
        )
        return(response)

    except botocore.exceptions.ClientError as error:
        raise error

def lambda_handler(event, context):
    try:
        #create_case()
        #describe_services()

        return {
            'statusCode': 200,
            'body': json.dumps(describe_services())
        }

    except botocore.exceptions.ClientError as error:
        raise error