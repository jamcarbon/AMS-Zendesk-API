http = urllib3.PoolManager()
zenpy_client = Zenpy(**creds)

def login():
    try:
        token = (user, pwd)
        headers = {'Authorization': f'token {token}'}
        r = http.request('GET', url,  headers=headers, body=json.dumps(token).encode('UTF-8'))
        data = json.loads(r.data)

def create_ticket():
    try:
        url = 'https://consegna.zendesk.com/api/v2/tickets.json'
        user = 'david.montenegro@consegna.cloud' + '/token'
        pwd = 'your_api_token'
        
        subject = 'THIS IS A TEST TICKET'
        body = 'PLEASE IGNORE'
        service = 'AWS Generic Tasks'
        impact = 'No Impact'
        Resolution_Code = 'Permanently Resolved'

        headers = {'Authorization': f'token {pwd}'}
        data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'service': service, 'impact': impact, 'Resolution_Code': Resolution_Code}}
        r = http.request('POST', url,  headers=headers, body=json.dumps(pwd).encode('UTF-8'))
        data = json.loads(r.data)



        if response.status_code != 201:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
        
        print(response)
        return response

    except botocore.exceptions.ClientError as error:
        raise error