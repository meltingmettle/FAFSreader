from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


#Switch to Python. 
#Use HTML parser on FAFS.
#For now, default to messaging one person. 
#Hard code items, and notifications.  Currently no price cap, since we're aiming for "larger" items.
#To be completed Winter Break 2018....

#Spreadsheet API implementation
#HTML Parser - the actual page reader
#Messenger Bots - use bottr.io



class Main:
  def __init__(self):
    self.reader = Reader()  #Constant.  The page should more or less always be the same
    self.itemList = Items("url to spreadsheet") #Possibly need login
  
class Items:
  #Will read items off a Google Doc
  items = []
  def __init__(self, spreadsheetID, itemRange): #Add price cap column later
    #Populate the list. Can add a price filter later. 
    # Setup the Sheets API
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.json')  #Either make the document public via link, or add a .json with login for an authorized account
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    RANGE_NAME = 'Class Data!A2:E'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        for v in values:
          items.append(v)
    

  
  #To get started
  #https://developers.google.com/api-client-library/python/apis/sheets/v4
  #https://developers.google.com/sheets/api/quickstart/python
 
class Reader:
   def __init__(self):
      return None
    
  def hit(x):
    #Array values are in descending order as specified by the range 
    messenger1 = InternalMessengerBot() #Pass in Item name
    messenger2 = ExternalMessengerBot() #Pass in User ID and Item Name or Message
    messenger1.sendMessage()
    messenger2.sendMessage()
    return None
  #This will return the Spreadsheet index of the found item when an item is found
  #values = result.get('values', [])
    
#Use Messenger API
class InternalMessengerBot
#This fellow might require a fake account.
  def __init__(self):
    return "My job is to message the client!"
  def

#A particularly well-designed Messenger Bot made by Wilson for a Hackathon
#We can do this in Python or Javascript.  
#https://github.com/AmaJC/BudgetBot/blob/master/budgetbot1/app.js

class ExternalMessengerBot:
#This will require a Messenger Account to be linked
  def __init__(self):
    return "My job is to message the sellers!"


@meltingmettle
@senorryan
@xX_surya_Xx
@avad_the_frosh

@cici_senor
@wilsonw926

#https://stackoverflow.com/questions/20045955/regex-pattern-in-python-for-parsing-html-title-tags
#https://developers.facebook.com/docs/messenger-platform/reference/send-api/
