import urllib.request, urllib.error, urllib.parse
import sys
import base64
import json
import os
import re

os.system("cls")
print(("-" * 80))
print ("Command Line Search Tool")
print(("-" * 80))

def Banner(text):
    print(("="*70))
    print (text)
    print(("="*70))
    sys.stdout.flush()

def sortByVotes():
    Banner('Sort By Votes')
    url = "http://www.commandlinefu.com/commands/browse/sort-by-votes/json"
    request = urllib.request.Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    str_reponse = response.readall().decode('utf-8')
    returnval = json.loads(str_reponse)
    for c in returnval:
        print(("-"*60))
        print((c['command']))

def sortByVotesToday():
    Banner('Printing All commands the last day (Sort By Votes) ')
    url = "http://www.commandlinefu.com/commands/browse/last-day/sort-by-votes/json"
    request = urllib.request.Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    str_reponse = response.readall().decode('utf-8')
    returnval = json.loads(str_reponse)
    for c in returnval:
        print(("-" * 60))
        print((c['command']))

def sortByVotesWeek():
    Banner('Printing All commands the last week (Sort By Votes) ')
    url = "http://www.commandlinefu.com/commands/browse/last-week/sort-by-votes/json"
    request = urllib.request.Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    str_reponse = response.readall().decode('utf-8')
    returnval = json.loads(str_reponse)
    for c in returnval:
        print(("-" * 60))
        print((c['command']))

def sortByVotesMonth():
    Banner('Printing: All commands from the last months (Sorted By Votes) ')
    url = "http://www.commandlinefu.com/commands/browse/last-month/sort-by-votes/json"
    request = urllib.request.Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    str_reponse = response.readall().decode('utf-8')
    returnval = json.loads(str_reponse)
    for c in returnval:
        print(("-" * 60))
        print((c['command']))

def sortByMatch():
    Banner("Sort By Match")
    match = input("Please enter a search command: ")
    bestmatch = re.compile(r' ')
    search = bytes(bestmatch.sub('+', match),'utf-8')
    b64_encoded = base64.b64encode(search)
    url = "http://www.commandlinefu.com/commands/matching/" + str(search) + "/" + str(b64_encoded)+ "/json"
    request = urllib.request.Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    returnval = json.loads(response.readall().decode('utf-8'))
    for c in returnval:
        print(("-" * 60))
        print((c['command']))

print ("""
1. Sort By Votes (All time)
2. Sort By Votes (Today)
3. Sort by Votes (Week)
4. Sort by Votes (Month)
5. Search for a command
Press enter to quit 
""")

while True:
    answer = input("What would you like to do? ")

    if answer == "":
        sys.exit()
    elif answer == "1":
        sortByVotes()
    elif answer == "2":
        print((sortByVotesToday()))
    elif answer == "3":
        print((sortByVotesWeek()))
    elif answer == "4":
        print((sortByVotesMonth()))
    elif answer == "5":
        print((sortByMatch()))
    else:
        print ("Not a valid choice")