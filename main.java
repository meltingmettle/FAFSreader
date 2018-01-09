import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.FileInputStream;
import java.io.jsoup;       \\Useful meme

\\This project will involve self-teaching and reading Java documentation, working with a few utils, and create a live, applied, and active system.
\\The biggest challenge will be verifying messages and reading the Free and For Sale Page, which both require authentication and a berkeley.edu account.
\\We need to be functional, fast, and accurate.  
\\ Matching non-exact reference: include "acostic guitar", "electric with missing string", NOT include "electric vacuum, guitar hero 6 CD"

\\Example code snippets
String html = "<p>An <a href='https://www.facebook.com/groups/BerkeleyFreeAndForSale/'><b>example</b></a> link.</p>";
Document doc = Jsoup.parse(html); 
String text = doc.body1).text(); 

//Need to authenticate via Facebook

Document doc = Jsoup.connect("https://www.facebook.com/groups/BerkeleyFreeAndForSale/").get();
log(doc.title());
Elements description = doc.select("#mp-itn b a");
for (Element item : description) {
  log("%s\n\t%s", 
    headline.attr("title"), headline.absUrl("href"));
}


class MainReader {
  String page;
  String LEPrecon;
  Ad[] adList;
  WantedItems[] bountyList;                                        \\Read this from a database-esque file
  \\OR
  File wantedItemsList;
  
  
  \\Will read and parse the page into tokens.
  \\Key aspects to read:                                \\Regex reacts only, please
  \\    item/header
  \\    price/"free"
  \\    seller messenger id (use the "Message seller" button
  \\    location/address (for AutoAssign challenge)
                             
    public void MainReader(String where, String who) {
      this.page = where;
      this.LEPrecon = who;
      
      {
    \\Compare every item name on the page to every wantedItem name
    \\Compare price iff item matches for efficiency
    \\Bonus points for whomeverestdly can design the fastest way to do this!
    public void runScan() {
     for (Ad a : Ad[] FreeAndForSale) {                 
         for (WantedItems i : WantedItems[] bountylist) {
           if itemMatches(i, a) {  \\Yeah boii
             MainMessenger comms = new MainMessenger(a.sellerID, i.LEPreconID)
             comms.sendMessage(message, a.sellerID, i.LEPreconID)
           }
                                
         } 
     }
      
    }
        
    public bool itemMatches(WantedItems item, Ad available) {
      if available.price.equals("free") or available.price <= item.priceMax {
        return True  
      } else {
        continue; 
      }
    }
  }


class MainMessenger {
  String[] message;   \\Need to work out the details on this.
  String sellerID;
  String LEPreconID;
  
  public bool MainMessenger(String sellerID, String pickupPerson) {
     this.message = message;  \\Messy.  Will clean up once final design develops a bit more
     this.sellerID = sellerID;
     this.LEPreconID = pickupPerson
  }
   
  public bool sendMessage(String[] message, String sellerID, String pickupPerson) {
    this.sellerID = sellerID;
    this.LEPreconID = pickupPerson;
    this.message = message;
    \\Message the person!
    \\Return true if the message goes through. 
    
    
  }
  
}
 
 class Ad {           \\Not sure if we will need this
   String item;
   String price;
   String sellerID;
   
   public bool Ad(String what, String howMuch, String who) {
    this.item = what;
    this.price = howMuch;
    this.sellerID = who;
     
   }
           
  class WantedItems {           \\This part might be a bit tricky. We will try to read from a File or spreadsheet or database
    String item;
    String priceMax;
    String whoNeeds;
    bool transportNeeded;
    File database;              \\Where is all this info going to be stored?
    
    public WantedItems(String theGood, String theBad, String theUgly, bool car) {
      this.item = theGood;
      this.price = theBad;
      this.whoNeeds = theUgly;
      this.transportNeeded = car;
    }
    
    
  }
   
 }
  
  
  \\Class responsible for messenging the seller with a pre-written message, taking the messenger ID from MainReader.
  \\Will also message a pick-up point man.  (For beta testing, me)
  }


public static void main(String[] args) {
   \\Let/'s go!
     
   \\Run a timed loop. Scan the page ~15 minutes.
}


Framework is as follows:
Step 1: Build a messenger bot
Step 2: Build a page reader
Step 3: Plug them into each other and start running a scan server
Step 4: ????????
Step 5: Profit


https://stackoverflow.com/questions/9825798/how-to-read-a-text-from-a-web-page-with-java
https://docs.oracle.com/javase/tutorial/networking/urls/readingURL.html
https://developers.facebook.com/docs/messenger-platform
https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start
https://github.com/fbsamples/messenger-platform-samples/tree/tutorial-starters/quick-start
