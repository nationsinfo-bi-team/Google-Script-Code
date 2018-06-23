
# coding: utf-8

# In[1]:


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
import requests
import json

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'D:/anaconda/client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


# In[2]:


# Sheet Definition
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


# In[3]:


# Dash Definition
def getsubset(data):
    l=[]
    for i in data:
        l.append(i)
    return l
def visit(data,i):
    return(data[getsubset(data)[i]])
def getwidget(data):
    return(data["widgets"])
def getPanel(widget):
    return(widget["metadata"]["panels"])
def panel(widget,string):
    t="not found"
    for i in range(len(getPanel(widget))):
        if getPanel(widget)[i]["name"]==string:
            t=getPanel(widget)[i]
            break
    return([t,i])

def getitem(panel):
    return(panel["items"])
def getjaql(item):
    return(item["jaql"])

def jaql(panel,string):
    t="not found"
    item=getitem(panel)
    for i in range(len(item)):
        if getjaql(item[i])["title"]==string:
            t=getjaql(item[i])
            break
    return([t,i])
            

def measure(context):
    t="t"
    if "dim" in context:
        t="Bottom"
    elif "type" in context:
        if context["type"]=="measure":
            t="Measure"
    elif len(context)>0 and "type" not in context:
        t="Collection"
    return(t)

def explorer(context,l=[],string="",count=0):
    
    if measure(context)=="Bottom":
        l.append(string+"|"+str(count)+"."+context["table"]+"|"+context["title"]+"|"+context["column"])
    if measure(context)=="Measure":
        count=count+1
        explorer(context["context"],l,string+"|"+str(count)+"."+context["title"],count)
    if measure(context)=="Collection":
        for i in context:
            explorer(context[i],l,string,count)
    return(l)

def metricMap(context,l=[],string="",count=0,l2=[],main="",cube=""):
    if measure(context)=="Bottom":
        if count==1:    
            c=[main,cube,context["table"],context["title"],context["column"]]
        elif count==0:
            c=[context["dim"],cube,context["table"],context["title"],context["column"]]
        else:
            c=[string,cube,context["table"],context["title"],context["column"]]
        if c not in l:
            l.append(c)
    if measure(context)=="Measure":
        count=count+1
        if count==1:
            mainm=context["title"]
            c1=[cube,mainm,mainm]
            if c1 not in l2:
                l2.append(c1)
            metricMap(context["context"],l,mainm,count,l2,mainm,cube)
        else:
            c2=[cube,main,context["title"]]
            c3=[cube,string,context["title"]]
            if c2 not in l2:
                l2.append(c2)
            if c3 not in l2:
                l2.append(c3)
            metricMap(context["context"],l,context["title"],count,l2,main,cube)
    if measure(context)=="Collection":
        for i in context:
            metricMap(context[i],l,string,count,l2,main,cube)
    return(l)
    


# In[62]:


# dash Api Call
headers={"Authorization":"Bearer " +"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiNWEzOTMzZjhkYzNjZjg1NmEwNDQxM2FmIiwiYXBpU2VjcmV0IjoiNjIwMDE4OGUtOWNmYi03MDVhLWZlNjktYzEyMDE4NTRhOTAxIiwiaWF0IjoxNTE4ODMyODQwfQ.IvZxMxOUlkRWMI_3agOkZUowZuxI5kjecqlfeyiwA2U"}
headers={"Authorization":"Bearer " +"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiNTU2ZmEzYWUzMTc4YWE4NDE3MDAwM2IwIiwiYXBpU2VjcmV0IjoiMTZhNjlhNzUtOTdhYS0zNmEyLTk2MjUtMTVhNzU1ZWI0YjhjIiwiaWF0IjoxNTIwOTY2Njc0fQ.qdz0Bl2Jv-5Rx26o5HyOZoyxDfzHMoyw_yZDhUQE2GY"}
url="http://52.37.229.249:8081/api/v1/dashboards"
dashes=json.loads(requests.get(url,headers=headers).text)


# In[74]:


l


# In[73]:


# Get values from Sisense to Write to Spreadsheet
values=[['Folder','Dashboard','Widget','Field_Type','DashID','Metrics','cube']]
metrics=[['cube','Metric','Subset']]
location=[['Metric','cube','table','title','column']]

for l in range(len(dashes)):
    try:
        oid=dashes[l]["oid"]
        daily=json.loads(requests.get(url+"/"+oid+"/export/dash",headers=headers).text)
        dname=daily["title"]
        cube=daily["datasource"]["title"]
        url1="http://52.37.229.249:8081/api/v1/folders/"+daily['parentFolder']
        folder=json.loads(requests.get(url1,headers=headers).text)
        if "parentId" in getsubset(folder):
            url1="http://52.37.229.249:8081/api/v1/folders/"+daily['parentFolder']+"/ancestors"
            foldername=json.loads(requests.get(url1,headers=headers).text)[0]["name"]
        else:
            foldername=folder["name"]
    except:
        continue

    for k in range(len(getwidget(daily))):
        try:
            widget=getwidget(daily)[k]
            wname=widget["title"]

            for j in range(len(getPanel(widget))):
                item=getitem(getPanel(widget)[j])
                name=getPanel(widget)[j]["name"]
                for i in range(len(getsubset(item))):
                    row=[foldername,dname,wname,name,daily["oid"],getjaql(item[i])["title"],cube]
                    values.append(row)
                    e=metricMap(getjaql(item[i]),location,"",0,metrics,"",cube)
        except:
            continue


# In[122]:


f="http://52.37.229.249:8081/api/v1/folders/59558f328e871e8c22000181"
c=json.loads(requests.get(f,headers=headers).text)


# In[34]:


oid=dashes[151]["oid"]
daily=json.loads(requests.get(url+"/"+oid+"/export/dash",headers=headers).text)
dname=daily["title"]
cube=daily["datasource"]["title"]
url1="http://52.37.229.249:8081/api/v1/folders/"+daily['parentFolder']
folder=json.loads(requests.get(url1,headers=headers).text)


# In[71]:


l


# In[160]:


if "parentId" in getsubset(folder):
    url1="http://52.37.229.249:8081/api/v1/folders/"+daily['parentFolder']+"/ancestors"
    foldername=json.loads(requests.get(url1,headers=headers).text)[0]["name"]
else:
    foldername=folder["name"]


# In[14]:


for k in range(len(getwidget(daily))):
   widget=getwidget(daily)[k]
   wname=widget["title"]
   


# In[15]:


values=[['Folder','Dashboard','Widget','Field_Type','DashID','Metrics','cube']]
metrics=[['cube','Metric','Subset']]
location=[['Metric','cube','table','title','column']]


# In[17]:


for j in range(len(getPanel(widget))):
   item=getitem(getPanel(widget)[j])
   name=getPanel(widget)[j]["name"]
   for i in range(len(getsubset(item))):
       row=[dname,wname,name,daily["oid"],getjaql(item[i])["title"],cube]
       values.append(row)
       e=metricMap(getjaql(item[i]),location,"",0,metrics,"",cube)


# In[21]:


location


# In[3]:


# Set up service
credentials=get_credentials()
http = credentials.authorize(httplib2.Http())
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')

service = discovery.build('sheets', 'v4', credentials=credentials)


# In[69]:


#parameter
spreadsheet_id = '1evarN1d8BwtbMLNXU4t6jLQ_4G23NCkqjoyLu7z0ZyE'
range_name = 'Dash!A1'
range1="Metric!A1"
range2="Table!A1"


# In[79]:


#read
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()
result.get('values', [])


# In[80]:


#write
body = {
    'values': values
}
result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id, range=range_name,
    valueInputOption="RAW", body=body).execute()


body = {
    'values': metrics
}
result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id, range=range1,
    valueInputOption="RAW", body=body).execute()

body = {
    'values': location
}
result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id, range=range2,
    valueInputOption="RAW", body=body).execute()

