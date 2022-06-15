import webbrowser
import random
import time

#path to edge app
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

#format for search
startquery = "https://www.bing.com/search?q="

#dictionary for random words and counter 
searchwords = ["amazon","2022","2021","google","weather","news","steam","facebook","youtube","monday",
               "tuesday","wednesday","thursday","friday","saturday","sunday","today","yesterday","stock","ebay",
               "brickseek","bidrl","reddit","bitcoin","gamestop","birthday","holiday","nba","nfl","US",
               "EU","ethereum","indeed","jobs","duckduckgo","google play","app store","walmart","target","best buy",
               "black friday","christmas","new year","lunar","steam sale","slickdeals","microsoft store","gog","craigslist","cag",
               "psn","xbox","coinbase","salesforce","glassdoor","epic","wikipedia","imdb","amazon prime","hulu",
               "peacock","disney plus"]
counter = 0

for x in range(35):
    randnum = random.randrange(len(searchwords))
    newsearch = startquery + searchwords[randnum]
    searchwords.pop(randnum)
    webbrowser.get('edge').open(newsearch)
    time.sleep(1.7)
    counter+=1

input("Completed " + str(counter) + " searches")


