from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time

"""
#PROJECT LIST
#For now, the messenger source and user will be hard-coded. 
1. HTML Parser - the actual page reader.  Check out BeautifulSoup.  Read the page and find desired items (considering typos) and the seller's messenger ID
2. Messenger Bots - use bottr.io. Create two messenging bots, one to message the seller and one to message the user. May require creating or linking to a FB account
3. Spreadsheet API implementation.  Read items and/or pricing or other parameters off a Google Spreadsheet.  Next-level involves allowing users to put their FBID on the sheet and get directly messaged instead of hard-code
"""

"""
Architecture notes:
Main will be called upon execution of the program. A Reader and SpreadsheetReader will be created. 
Every day around 3:00PM, FAFSreader will call spreadsheet.update() for updates on items or users
Main will periodically call Reader().read which will read FAFS and look for said items.
Reader will read Free and For Sale, then if it finds an item, it will generate a messenger bot with the user's id and a bot with the seller's id.
The messenger bot will tell the user that an item has been found, and it will message the seller expressing interest in buying.  

"""
"""
Page Reader docs:  Check out Beautiful Soup toolkit!
https://stackoverflow.com/questions/20045955/regex-pattern-in-python-for-parsing-html-title-tags
https://developers.facebook.com/docs/messenger-platform/reference/send-api/

Google Spreadsheet API docs
https://developers.google.com/api-client-library/python/apis/sheets/v4
https://developers.google.com/sheets/api/quickstart/python

Messenger Bots docs
http://bottr.co/
https://github.com/geeknam/messengerbot
https://github.com/AmaJC/BudgetBot/blob/master/budgetbot1/app.js

"""

class Main:
  def __init__(self):
    self.reader = Reader()  #Constant.  The page should more or less always be the same. Will update if URl changes.
    self.itemList = Items("url to spreadsheet") #Possibly need login
    while true:
      time.sleep(600)
      reader.run()
      #Run the reader every 10 minutes
      
    
class SpreadsheetReader:
  def __init__(self, sheet_url):
    self.sheet = sheet_url
    #Add reader here
  def update(self):
    return "Update items and users from spreadsheet"
  
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
    

 
class Reader:
   def __init__(self):
      return None
   
   def read():
      #Put the HTML parser here.
      return None
    
   def success(x):
      #Array values are in descending order as specified by the range 
      messenger1 = InternalMessengerBot() #Pass in Item name
      messenger2 = ExternalMessengerBot() #Pass in User ID and Item Name or Message
      messenger1.sendMessage()
      messenger2.sendMessage()
      return None
  #This will return the Spreadsheet index of the found item when an item is found
  #values = result.get('values', [])
    
#Use Messenger API
class InternalMessengerBot:
#This fellow might require a fake account.
  def __init__(self):
    return "My job is to message the client!"

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


