import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.FileInputStream;


class AutoAssign {
  \\If the page-parser detects a general location or an address, this will also autoassign and message the person who is closest and available to make the pick-up.
  \\Slightly easier variation of the messenger bot
   
  protected database;            \\Let's not have our addresses floating on the internet :) 
   
  private void deployScout(bool transport) {
  \\Take in a house location, the point person, and then message the person.
  \\If it's a large item and we need a transport, it will message the closest person with a van.
  
  }
  
 
 class HouseDB {
 House[] houses;
 
   public HouseDB(House[] house) {
      this.houses = house;
   }
   
   private House nearestFOB(int[] dropCoords) {
      \\Find the nearest house.  Basic mathmatical function with a mapping. :)
      return nearestBase
   }
   
 }
 
 class House {
   int range;                   \\As a challenge, can we plug house to drop coordinates to Google Maps and accurately asses travel time?
   bool vehicle;
   String headOfState;          \\Messenger profile of House Head
   int[] coord;                 \\Throwback to Yelp Maps Project
   bool armor;
   
   protected House(bool v, String hOS, int[] coordinates, bool bretheren) {
      this.vehicle = v;
      this.headOfState = hOS
      this.coord = coordinates
      this.armor = bretheren
   }
   
 
 
 
 }


    public static void main(String[] args) {
        \\
    }
}
