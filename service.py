import flask
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']

def get_credentials(credentials):
    creds = Credentials(
        credentials['token']
    )
    service = build('people', 'v1', credentials=creds)
    results = service.people().connections().list(
        resourceName='people/me',
        pageSize=1500,
        personFields='names,emailAddresses,phoneNumbers').execute()
    connections = results.get('connections', [])
    return connections