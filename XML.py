
# coding: utf-8

# In[5]:


from datetime import datetime
import xml.etree.ElementTree


# In[11]:


log=open("C:/Users/Shuting Zhao/Desktop/Archive/python/csr log.xml").read()
e = xml.etree.ElementTree.parse("C:/Users/Shuting Zhao/Desktop/Archive/python/csr log.xml").getroot()
ec=e[0]
cube=ec


# In[7]:


def getlist(ec):
    l=[]
    for child in ec:
        print(child.tag,child.attrib,child.text)
getlist(ec[11][15][11][0])


# In[97]:


def subset(ec):
    l=[]
    for child in ec:
        l.append(child.tag)
    return(l)

def xmlexplorer(ec,l=[],string="",t=""):
    if "Title" in subset(ec):
        if ec[0].text=="Building" or ec[0].text=="Finalizing Build" or ec[0].text=="Initializing":
            l.append(string+"|" + ec[2].text )
            xmlexplorer(ec[11],l,string,ec[2].text)
        elif ec[0].text=="Successfully built" or ec[0].text=="Finalization Completed" or ec[0].text=="Initialization completed":
            l[len(l)-1]=l[len(l)-1]+"|" + ec[3].text+"|"+str((datetime.strptime(ec[3].text, '%m/%d/%Y %I:%M:%S %p')-datetime.strptime(t, '%m/%d/%Y %I:%M:%S %p')).total_seconds())
        ##else: 
            ##xmlexplorer(ec[11],l,string)
    else:
        for child in ec:
            xmlexplorer(child,l,string,t)
    return(l)


# In[120]:


len(l)


# In[119]:


l=[]
j=0
for i in range(0,len(cube[11])):
   
    if cube[11][i].attrib["CloudColumn"]!="":
        col="custom"+"|"+cube[11][i].attrib["CloudColumn"]
        j=1
    elif j>0 and  cube[11][i][0].text=="Building":
        col="custom"+"|"+"table"
    elif cube[11][i][0].text=="Building" :
        col="raw"+"|"+"table"
    else:
        col=cube[11][i][0].text+"|null"
    xmlexplorer(cube[11][i],l,str(i)+"|"+col+"|"+cube[11][i].attrib["CloudTable"])
l


# In[38]:


t1="2/14/2018 5:25:54 AM"
datetime.strptime(t1, '%m/%d/%Y %I:%M:%S %p')


# In[117]:


len(cube[11])


# In[118]:


l=[]
j=0
for i in range(2,78):
   
    if cube[11][i].attrib["CloudColumn"]!="":
        col="custom"+"|"+cube[11][i].attrib["CloudColumn"]
        j=1
    elif j>0:
        col="custom"+"|"+"null"
    else:
         col="raw"+"|"+"null"
    xmlexplorer(cube[11][i],l,str(i)+"|"+col+"|"+cube[11][i].attrib["CloudTable"])
l


# In[85]:


j

