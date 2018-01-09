import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.FileInputStream;


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
