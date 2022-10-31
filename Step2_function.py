import boto3
import botocore.exceptions
import json
import logging
from botocore.vendored import requests
import urllib3

http = urllib3.PoolManager()
client = boto3.client('support')

language = "en"

def create_ticket(event):
    try:
        url = 'https://consegna.zendesk.com/api/v2/tickets.json'
        user = 'test@email.com' + '/token'
        pwd = 'tokengeneratedfromzendesk'
        
        subject = event["subject"]

        ticket_details = {'displayId': event['displayId'], 'severityCode': event['severityCode']}

        body_raw = """Amazon Web Services has opened case {displayId} on your behalf.

        The details of your case are as follows:

        Case ID: {displayId}
        Severity: {severityCode}


        To contact us again about this issue, please reply to this Zendesk ticket.
        Please use the following link to attach any files you think would be useful:

        https://console.aws.amazon.com/support/home#/case/?displayId={displayId}&language=en

        (If you will connect by federation, log in before following the link.)


        Sincerely,
        The Amazon Web Services Team

        *Please note: this e-mail was sent from an address that cannot accept incoming e-mail. Please use the appropriate link above if you need to contact us again about this same issue.

        Amazon Web Services, Inc. is an affiliate of Amazon.com, Inc. Amazon.com is a registered trademark of Amazon.com, Inc. or its affiliates.

        Some of the content and links in this email may have been generated by an Amazon customer. Amazon is not responsible for the contents or links within."""

        body = body_raw.format(**ticket_details)
        service = 'AWS Generic Tasks'
        impact = 'No Impact'
        Resolution_Code = 'Permanently Resolved'
        priority = event["severityCode"]

        headers = {'content-type': 'application/json'}
        #data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'service': service, 'impact': impact, 'Resolution_Code': Resolution_Code}}
        #data = {'ticket': {'subject': subject, 'priority': priority,'comment': {'body': body}}}
        data = {'ticket': {'subject': subject,'comment': {'body': body}}}
        payload = json.dumps(data)
        #r = http.request('POST', url, auth=(user, pwd), headers=headers, data=payload)
        response = requests.post(url, data=payload, auth=(user, pwd), headers=headers)
        rjson = response.json()
        
        print(type(rjson))
        print(rjson)

        #add Zendesk Ticket number as a body on the second reply of AMS
        add_zendesk_ticketn(response)

        return response
    
    except botocore.exceptions.ClientError as error:
        raise error

def add_zendesk_ticketn(event):
    ticket_id = event["ticket"]["id"]
    response = client.add_communication_to_case(
        caseId=ticket_id,
        communicationBody=ticket_id
    )
    return response

def update_ticket(event):
    try:
        nofcases = event["recentCommunications"]["communications"]
        idn = len(nofcases) - 2
        tid = event["recentCommunications"]["communications"][idn]

        url = 'https://consegna.zendesk.com/api/v2/tickets.json' + tid + '.json'
        user = 'david.montenegro@consegna.cloud' + '/token'
        pwd = 'tokengeneratedfromzendesk'
        
        subject = event["subject"]
        body = event["recentCommunications"]["communications"][0]["body"]
        print(body)
        service = 'AWS Generic Tasks'
        impact = 'No Impact'
        Resolution_Code = 'Permanently Resolved'

        headers = {'content-type': 'application/json'}
        #data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'service': service, 'impact': impact, 'Resolution_Code': Resolution_Code}}
        data = {'ticket': {'comment': {'body': body, "public": true}}}
        payload = json.dumps(data)
        response = requests.post(url, data=payload, auth=(user, pwd), headers=headers)
        rjson = response.json()
        
        print(type(rjson))
        print(rjson)
        return response
    
    except botocore.exceptions.ClientError as error:
        raise error

def get_ticket():
    try:
        id = '40879'
        body = 'Thanks for choosing Acme Jet Motors.'
        url = 'https://consegna.zendesk.com/api/v2/tickets/41172'
        user = 'david.montenegro@consegna.cloud' + '/token'
        pwd = 'tokengeneratedfromzendesk'
        
        
        headers = {'content-type': 'application/json'}
        
        #r = http.request('GET', url, auth=(user, pwd), headers=headers)
        response = requests.get(url, auth=(user, pwd), headers=headers)
        rjson = response.json()
        
        print(type(rjson))
        print(rjson)
        return response
    
    except botocore.exceptions.ClientError as error:
        raise error
        
def get_brands():
    try:
        body = 'Thanks for choosing Acme Jet Motors.'
        url = 'https://consegna.zendesk.com/api/v2/brands'
        user = 'david.montenegro@consegna.cloud' + '/token'
        pwd = 'tokengeneratedfromzendesk'
        
        
        headers = {'content-type': 'application/json'}
        
        response = requests.get(url, auth=(user, pwd), headers=headers)
        #data = json.loads(response)
        print(type(response))
        rjson = response.json()
        
        #parsed = json.loads(rjson)
        #print(json.dumps(rjson, indent=4))
        print(type(rjson))
        print(rjson)
        return response
    
    except botocore.exceptions.ClientError as error:
        raise error
        
def get_ticketfields():
    try:
        url = 'https://consegna.zendesk.com/api/v2/ticket_fields'
        user = 'david.montenegro@consegna.cloud' + '/token'
        pwd = 'tokengeneratedfromzendesk'
        
        headers = {'content-type': 'application/json'}
        
        response = requests.get(url, auth=(user, pwd), headers=headers)
        #data = json.loads(response)
        print(type(response))
        rjson = response.json()
        
        #parsed = json.loads(rjson)
        #print(json.dumps(rjson, indent=4))
        print(type(rjson))
        print(rjson)
        return response
    
    except botocore.exceptions.ClientError as error:
        raise error

def describe_cases(event):
    try:
        ams_case_id = event["detail"]["responseElements"]["caseId"]
        response1 = client.describe_cases(
            caseIdList=[
                ams_case_id,
            ],
            includeResolvedCases=True,
            language=language,
            includeCommunications=True
        )
    
        return(response1)

    except botocore.exceptions.ClientError as error:
        raise error

def lambda_handler(event, context):
    try:
        #print(event)

        #ticket_info = get_ticket(event)

        #main
        eventDetailType = event["detail-type"]
        eventName = event["detail"]["eventName"]
        ticket_data = describe_cases(event)

        if eventDetailType == "AWS API Call via CloudTrail":
            if eventName == "CreateCase":
                create_ticket(ticket_data)
            elif eventName == "AddCommunicationToCase":
                update_ticket(ticket_data)

        else:
            return "There was no event from CLoudTrail"

        reply = "Zendesk ticket created"
        ticket_json = ticket_info.json()
        
        print(ticket_json)
        print(type(ticket_json))

        return ticket_json

    except botocore.exceptions.ClientError as error:
        raise error