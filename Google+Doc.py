
# coding: utf-8

# In[ ]:


from pprint import pprint
import requests
from googleapiclient import discovery
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


# In[123]:


flags = None
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'D:/anaconda/client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


# In[124]:


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


# In[129]:





# In[130]:


credentials=get_credentials()
http = credentials.authorize(httplib2.Http())
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')

service = discovery.build('sheets', 'v4', credentials=credentials)


# In[102]:



spreadsheet_id = '1evarN1d8BwtbMLNXU4t6jLQ_4G23NCkqjoyLu7z0ZyE'
range_name = 'Dash!A1'


# In[132]:


#write
values = [
    [
      111,222  # Cell values ...
    ],
    [333,444]
    # Additional rows
]
body = {
    'values': values
}
result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id, range=range_name,
    valueInputOption="RAW", body=body).execute()


# In[101]:


#read
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheetId, range=rangeName).execute()
result.get('values', [])

