from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time

"""
#PROJECT LIST
I'm currently implementing the Facebook Page reader.  
Unfortunately, later on we might need to move to a private repo to protect access tokens, but we can make a public copy. 

1. HTML Parser - Check out BeautifulSoup.  Read the page and find desired items (considering typos) and the seller's messenger ID
   - Read .json files and extract the item, price, and seller ID.  Check out this post on web-scraping: https://github.com/minimaxir/facebook-page-post-scraper/blob/master/examples/how_to_build_facebook_scraper.ipynb
2. Messenger Bots - use bottr.io. Create two messenging bots, one to message the seller and one to message the user. May require creating or linking to a FB account
   - Involves autheticating two app-bots. 
   - Parse and send a message and possibly include a screenshot/link to the post
3. Spreadsheet API implementation.  Read items and/or pricing or other parameters off a Google Spreadsheet.  Next-level involves allowing users to put their FBID on the sheet and get directly messaged instead of hard-code
   - More tedious authentication procedure, but shouldn't be too difficult. Check out the docs provided below.
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

#TODO: create an algorithm to discern price.  (IE Some posts say "$40 amp and $15 cables", while others will say "bike - $60, table $10")
class Main:
  def __init__(self):
    self.itemList = Items("url to spreadsheet") #Possibly need login
    self.reader = Reader(self.itemList)  #Constant.  The page should more or less always be the same. Will update if URl changes.
    #Refresh itemslist?
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
  wantedItems = []
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
          wantedItems.append(v)
    

class Item:
   def __init__(self, name, seller_id, price):
      self.name = name
      self.seller_id = seller_id
      self.price = price
   
   def getName(self):
      return self.name
   
   def getSeller_id(self):
      return self.sellerID
   
   def getPrice(self):
      return self.price
   
   
class Reader:
   def __init__(self, wantedItems):
      self.items = wantedItems
      self.pageResults = {} #Key should be string of item name, value should be Item object with all parameters
      return None
          
   def pageRequest():
      #This will return a huge list/file of item names and corresponding item objects
      results = "not quite there yet"                    
      return read(results)
   
   def read(posts):
      #Take in page data and format it. Read the item names, adding the name to pageResults, and creating an Item object to add to pageResultsList.
      #Dictionary format should be {"guitar": <Item object ... "guitar">, "chairs" : <Item object ..>}"
      
      #Put the HTML parser here.
      #TODO Split by words and search each word individually
      #How can we narrow down the searcH? (IE Dining table, and not table, folding table, broken table)
      search()
      
   def search():
      for i in items:
         if i in pageResults:
            success(pageResults[i])
      pageResults = {}
      return None

     
   def success(x): #Input is an item object with item, price, and seller ID
      #Array values are in descending order as specified by the range 
      #TODO: Avoid annoying false negatives
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


