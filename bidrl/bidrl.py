#Web scraping the site bidrl 

import json
import requests
import datetime
import time
import webbrowser

#Current date and time 
currenttime = datetime.datetime.now()
currentunixtime = time.time()

print ("Today is " + str(currenttime.date()) + ".\nThe time is " + str(currenttime.time()) + "\n")

# read all data

#Spage = requests.get("https://www.bidrl.com/api/landingPage/sacramento-2")
Spage = requests.get("https://www.bidrl.com/api/landingPage/cesar-lua-2")
Sjson = Spage.json()
Epage = requests.get("https://www.bidrl.com/api/landingPage/elk-grove-8")
Ejson = Epage.json()
Rpage = requests.get("https://www.bidrl.com/api/landingPage/rancho-cordova-34")
Rjson = Rpage.json()
Cpage = requests.get("https://www.bidrl.com/api/landingPage/citrus-heights-37")
Cjson = Cpage.json()
Npage = requests.get("https://www.bidrl.com/api/landingPage/natomas-39")
Njson = Npage.json()
Gpage = requests.get("https://www.bidrl.com/api/landingPage/galt-7")
Gjson = Gpage.json()
ESpage = requests.get("https://www.bidrl.com/api/landingPage/east-sacramento-45")
ESjson = ESpage.json()

print ("There are " + str(Sjson['total']) + " auction galleries available at Sacramento.")
print ("There are " + str(Ejson['total']) + " auction galleries available at Elk Grove.")
print ("There are " + str(Rjson['total']) + " auction galleries available at Rancho Cordova.")
print ("There are " + str(Cjson['total']) + " auction galleries available at Citrus Heights.")
print ("There are " + str(Njson['total']) + " auction galleries available at Natomas.")
print ("There are " + str(Gjson['total']) + " auction galleries available at Galt.")
print ("There are " + str(ESjson['total']) + " auction galleries available at East Sacramento.\n")
print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

#Json page which has all auction item information
getitems = "https://www.bidrl.com/api/getitems"

#Finding out the auction id of most recent gallery that is not closed
for Sauctions in Sjson['auctions'].keys():
    if Sjson['auctions'][Sauctions]['status'] == "open":
        S_Id = Sjson['auctions'][Sauctions]['id']
        break
    
#Elk Grove Json page is not a dictionary but a list for some reason
for Eauctions in range(len(Ejson['auctions'])):
    if (Ejson['auctions'][Eauctions]['status'] == "open"):
        E_Id = Ejson['auctions'][Eauctions]['id']
        break
    
for Rauctions in Rjson['auctions'].keys():   
    if Rjson['auctions'][Rauctions]['status'] == "open":
        R_Id = Rjson['auctions'][Rauctions]['id']
        break
        
for Cauctions in Cjson['auctions'].keys():
    if Cjson['auctions'][Cauctions]['status'] == "open":
        C_Id = Cjson['auctions'][Cauctions]['id']
        break

for Nauctions in Njson['auctions'].keys():    
    if Njson['auctions'][Nauctions]['status'] == "open":
        N_Id = Njson['auctions'][Nauctions]['id']
        break

for Gauctions in Gjson['auctions'].keys():    
    if Gjson['auctions'][Gauctions]['status'] == "open":
        G_Id = Gjson['auctions'][Gauctions]['id']
        break

for ESauctions in range(len(ESjson['auctions'])):
    if (ESjson['auctions'][str(ESauctions+1)]['status'] == "open"):
        ES_Id = ESjson['auctions'][str(ESauctions+1)]['id']
        break
   
#Putting it into format for POST to getitems json page
SItems = {"auction_id": S_Id,}
EItems = {"auction_id": E_Id,}
RItems = {"auction_id": R_Id,}
CItems = {"auction_id": C_Id,}
NItems = {"auction_id": N_Id,}
GItems = {"auction_id": G_Id,}
ESItems = {"auction_id": ES_Id,}

#Retrieves item information from most recent gallery
SPost = requests.post(getitems, data = SItems).json()
EPost = requests.post(getitems, data = EItems).json()
RPost = requests.post(getitems, data = RItems).json()
CPost = requests.post(getitems, data = CItems).json()
NPost = requests.post(getitems, data = NItems).json()
GPost = requests.post(getitems, data = GItems).json()
ESPost = requests.post(getitems, data = ESItems).json()


SItem1 = SPost['items'][0]['title']
EItem1 = EPost['items'][0]['title']
RItem1 = RPost['items'][0]['title']
CItem1 = CPost['items'][0]['title']
NItem1 = NPost['items'][0]['title']
GItem1 = GPost['items'][0]['title']
ESItem1 = ESPost['items'][0]['title']



#For some reason Galt json starts out with 2
Stimes = Sjson['auctions']['2']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
Etimes = Ejson['auctions'][0]['info_div'].replace("<b>"," ").replace("</b>","").replace("<br>","").replace("<br />","")
Rtimes = Rjson['auctions']['1']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
Ctimes = Cjson['auctions']['1']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
Ntimes = Njson['auctions']['1']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
Gtimes = Gjson['auctions']['3']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
EStimes = ESjson['auctions']['1']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")


#Calculating the time left before the first item closes
SItemtime = float(SPost['items'][0]['ends']) + 7200
Stimeleft = SItemtime - currentunixtime
EItemtime = float(EPost['items'][0]['ends']) + 7200
Etimeleft = EItemtime - currentunixtime
RItemtime = float(RPost['items'][0]['ends']) + 7200
Rtimeleft = RItemtime - currentunixtime
CItemtime = float(CPost['items'][0]['ends']) + 7200
Ctimeleft = CItemtime - currentunixtime
NItemtime = float(NPost['items'][0]['ends']) + 7200
Ntimeleft = NItemtime - currentunixtime
GItemtime = float(GPost['items'][0]['ends']) + 7200
Gtimeleft = GItemtime - currentunixtime
ESItemtime = float(ESPost['items'][0]['ends']) + 7200
EStimeleft = ESItemtime - currentunixtime


Rauctionlink = Rjson['auctions']['1']['auction_id_slug']

#Seems to only be for the Rancho Cordova location
def Oneitem(location,ID):
    if (location == "R"):
        RPost = requests.post("https://www.bidrl.com/api/ItemData", data = {"item_id": ID,}).json()
        RItemtime = float(RPost['end_time']) + 7200
        Rtimeleft = RItemtime - currentunixtime
        print ("This item will close in " + str(datetime.timedelta(seconds = Rtimeleft)))        
        print (Rtimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" + Rauctionlink + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

#Information on the most recent auction and when the first item closes
if Stimes.find("First Item Closes") != -1:
    print ("The first auction gallery in Sacramento is a " + (Sjson['auctions']['2']['title']))
    print ("The first item in this gallery is titled " + SItem1 + ".")
    print ("The first item's current bid is at $" + SPost['items'][0]['current_bid'] + ".")
    print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(SPost['items'][0]['current_bid']) * .082525 + float(SPost['items'][0]['current_bid']) + float(SPost['items'][0]['current_bid']) * .13))
    if (Stimeleft < 0):
        print ("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||| \nThe current gallery is closing items right now!\n||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    else:
        print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Stimeleft)))
    print (Stimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Sjson['auctions']['2']['auction_id_slug']  + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

else:
    Stimes = Sjson['auctions']['3']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    print ("An auction has recently closed. The next auction gallery in Sacramento is a " + (Sjson['auctions']['3']['title']))
    print (Stimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Sjson['auctions']['3']['auction_id_slug'] + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")
    

if Etimes.find("First Item Closes") != -1:
    print ("The first auction gallery in Elk Grove is a " + (Ejson['auctions'][0]['title']))
    print ("The first item in this gallery is titled " + EItem1 + ".")
    print ("The first item's current bid is at $" + EPost['items'][0]['current_bid'] + ".")
    print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(EPost['items'][0]['current_bid']) * .0825 + float(EPost['items'][0]['current_bid']) + float(EPost['items'][0]['current_bid']) * .13))
    if (Etimeleft < 0):
        print ("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||| \nThe current gallery is closing items right now!\n||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    else:
        print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Etimeleft)))
    print (Etimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Ejson['auctions'][0]['auction_id_slug']  + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

else:
    Etimes = Ejson['auctions'][1]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    print ("An auction has recently closed. The next auction gallery in Elk Grove is a " + (Ejson['auctions'][1]['title']))
    print (Stimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Ejson['auctions'][1]['auction_id_slug']  + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")
    
if Rtimes.find("First Item Closes") != -1 or Rtimes.find("Closing Time") != -1:
    print ("The first auction gallery in Rancho Cordova is a " + (Rjson['auctions']['1']['title']))
    print ("The first item in this gallery is titled " + RItem1 + ".")
    print ("The first item's current bid is at $" + RPost['items'][0]['current_bid'] + ".")
    print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(RPost['items'][0]['current_bid']) * .0825 + float(RPost['items'][0]['current_bid']) + float(RPost['items'][0]['current_bid']) * .13))
    if (Rjson['auctions']['1']['item_count'] == "1"):
        Rauctionlink = Rjson['auctions']['1']['id'] + "/item/" + Rjson['auctions']['1']['item_id_slug']
        Oneitem("R",Rjson['auctions']['1']['item_id'])
    else:
        if (Rtimeleft < 0):
            print ("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||| \nThe current gallery is closing items right now!\n||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
        else:
            print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Rtimeleft)))
        print (Rtimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Rjson['auctions']['1']['auction_id_slug'] + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

else:
    Rtimes = Rjson['auctions']['2']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    print ("An auction has recently closed. The next auction gallery in Rancho Cordova is a " + (Rjson['auctions']['2']['title']))
    print (Rtimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Rjson['auctions']['2']['auction_id_slug'] + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    
if Ctimes.find("First Item Closes") != -1:
    print ("The first auction gallery in Citrus Heights is a " + (Cjson['auctions']['1']['title']))
    print ("The first item in this gallery is titled " + CItem1 + ".")
    print ("The first item's current bid is at $" + CPost['items'][0]['current_bid'] + ".")
    print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(CPost['items'][0]['current_bid']) * .0825 + float(CPost['items'][0]['current_bid']) + float(CPost['items'][0]['current_bid']) * .13))
    if (Ctimeleft < 0):
        print ("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||| \nThe current gallery is closing items right now!\n||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    else:
        print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Ctimeleft)))
    print (Ctimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Cjson['auctions']['1']['auction_id_slug']  + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

else:
    Ctimes = Cjson['auctions']['2']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    print ("An auction has recently closed. The next auction gallery in Citrus Heights is a " + (Cjson['auctions']['2']['title']))
    print (Ctimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Cjson['auctions']['2']['auction_id_slug'] + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")


if Ntimes.find("First Item Closes") != -1:
    print ("The first auction gallery in Natomas is a " + (Njson['auctions']['1']['title']))
    print ("The first item in this gallery is titled " + NItem1 + ".")
    print ("The first item's current bid is at $" + NPost['items'][0]['current_bid'] + ".")
    print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(NPost['items'][0]['current_bid']) * .0825 + float(NPost['items'][0]['current_bid']) + float(NPost['items'][0]['current_bid']) * .13)) 
    if (Ntimeleft < 0):
        print ("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||| \nThe current gallery is closing items right now!\n||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    else :    
        print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Ntimeleft)))
    print (Ntimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Njson['auctions']['1']['auction_id_slug']  + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

else:
    Ntimes = Njson['auctions']['2']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    print ("An auction has recently closed. The next auction gallery in Natomas is a " + (Njson['auctions']['2']['title']))
    print (Ntimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Njson['auctions']['2']['auction_id_slug'] + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")


if Gtimes.find("Closing Time") != -1 or Gtimes.find("First Item Closes") != -1:
    print ("The first auction gallery in Galt is a " + (Gjson['auctions']['3']['title']))
    print ("The first item in this gallery is titled " + GItem1 + ".")
    print ("The first item's current bid is at $" + GPost['items'][0]['current_bid'] + ".")
    print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(GPost['items'][0]['current_bid']) * .0825 + float(GPost['items'][0]['current_bid']) + float(GPost['items'][0]['current_bid']) * .13))
    if (Gtimeleft < 0):
        print ("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||| \nThe current gallery is closing items right now!\n||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    else :    
        print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Gtimeleft)))
    print (Gtimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Gjson['auctions']['3']['auction_id_slug']  + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

else:
    Gtimes = Gjson['auctions']['3']['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    print ("An auction has recently closed. The next auction gallery in Galt is a " + (Gjson['auctions']['4']['title']))
    print (Gtimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Gjson['auctions']['4']['auction_id_slug'] + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

if EStimes.find("First Item Closes") != -1:
    print ("The first auction gallery in East Sacramento is a " + (ESjson['auctions']['1']['title']))
    print ("The first item in this gallery is titled " + ESItem1 + ".")
    print ("The first item's current bid is at $" + ESPost['items'][1]['current_bid'] + ".")
    print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(ESPost['items'][0]['current_bid']) * .082525 + float(ESPost['items'][0]['current_bid']) + float(ESPost['items'][0]['current_bid']) * .13))
    if (EStimeleft < 0):
        print ("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||| \nThe current gallery is closing items right now!\n||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    else:
        print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = EStimeleft)))
    print (EStimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  ESjson['auctions']['1']['auction_id_slug']  + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

else:
    EStimes = ESjson['auctions'][1]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    print ("An auction has recently closed. The next auction gallery in East Sacramento is a " + (ESjson['auctions'][1]['title']))
    print (EStimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  ESjson['auctions'][1]['auction_id_slug'] + "\n")
    print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

#Finding out where edge is located on computer to open web page
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

#Cannot get firefox to open up. Using edge to open web browser as of 6/5/2022
#firefox_path = "C:\Program Files\Mozilla Firefox\firefox.exe"
#webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

Startlink = "https://www.bidrl.com/auction/"

#Input to open web page to auction gallery
Redirectto = input("Please type a location to go to or type in 'Exit' to exit: ")
while Redirectto != "No":
    try:
        if (Redirectto == "Sacramento" or Redirectto == "sacramento" or Redirectto == 's' or Redirectto == 'S'):
            print ("Opening up the most recent Sacramento gallery.\n")
            Fulllink = Startlink + Sjson['auctions']['2']['auction_id_slug']
            webbrowser.get('edge').open(Fulllink)
        elif (Redirectto == "Exit" or Redirectto == "exit"):
            print ("Exiting program")
            break
        elif (Redirectto == "Elk Grove" or Redirectto == "elk grove" or Redirectto == "elkgrove" or Redirectto == "Elkgrove" or Redirectto == 'e' or Redirectto == 'E'):
            print ("Opening up the most recent Elk Grove gallery.\n")
            Fulllink = Startlink + Ejson['auctions'][1]['auction_id_slug']
            webbrowser.get('edge').open(Fulllink)
        elif (Redirectto == "Rancho Cordova" or Redirectto == "rancho cordova" or Redirectto == "ranchocordova" or Redirectto == "Ranchocordova" or Redirectto == 'r' or Redirectto == 'R' or Redirectto == "Rancho" or Redirectto == "rancho"):
            print ("Opening up the most recent Rancho Cordova gallery.\n")
            Fulllink = Startlink + Rauctionlink
            webbrowser.get('edge').open(Fulllink)
        elif (Redirectto == "Citrus Heights" or Redirectto == "citrus heights" or Redirectto == "citrusheights" or Redirectto == "Citrusheights" or Redirectto == 'C' or Redirectto == 'c'):
            print ("Opening up the most recent Citrus Heights gallery.\n")
            Fulllink = Startlink + Cjson['auctions']['1']['auction_id_slug']
            webbrowser.get('edge').open(Fulllink)
        elif (Redirectto == "Natomas" or Redirectto == "natomas" or Redirectto == 'n' or Redirectto == 'N'):
            print ("Opening up the most recent Natomas gallery.\n")
            Fulllink = Startlink + Njson['auctions']['1']['auction_id_slug']
            webbrowser.get('edge').open(Fulllink)
        elif (Redirectto == "Galt" or Redirectto == "galt" or Redirectto == 'g' or Redirectto == 'G'):
            print ("Opening up the most recent Galt gallery.\n")
            Fulllink = Startlink + Gjson['auctions']['3']['auction_id_slug']
            webbrowser.get('edge').open(Fulllink)
        elif (Redirectto == "East Sacramento" or Redirectto == "east sacramento" or Redirectto == 'es' or Redirectto == 'ES' or Redirectto == 'Es' or Redirectto == 'east' or Redirectto == 'East'):
            print ("Opening up the most recent East Sacramento gallery.\n")
            Fulllink = Startlink + ESjson['auctions']['1']['auction_id_slug']
            webbrowser.get('edge').open(Fulllink)
        else:
            print("Keyword not valid or recognized. Please type again:")
        Redirectto = input("Please type a location to go to or type in 'Exit' to exit: ")
    except KeyError:
        print ("There has been an error in opening up the gallery. It will be fixed shortly.")


#6/8/2022 Added more options to redirect to webpages
#6/7/2022 Added Galt to locations it finds info on.
#6/5/2022 Added prompt and redesigned search to pass more test cases
#6/1/2022 JSON Page switched to name cesar-lua for some reason for Sacramento json page
