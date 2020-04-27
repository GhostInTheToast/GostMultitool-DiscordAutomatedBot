import json
import os
from urllib.request import urlopen
from pathlib import Path
from random import randint as randint
import requests

# Path logic
path = Path(os.getcwd())
levels_up = 1

steam_string = open(str(path) + '\\json\\' + 'steamstuff.json','r',encoding='utf-8')
newSteamString = urlopen("https://api.steampowered.com/ISteamApps/GetAppList/v2")

# Path Logic End

# BINGOOOOO print(data['app'])
data = json.load(steam_string)
steamJson = json.loads(newSteamString.read())

# Not used anymore, new one in place which looks cleaner and more careful
def Old_steamGameSearch(game_name):
    id = 1

    for game in data["app"]:
        #print(game['name'])

        if game_name.lower() == str(game['name']).lower():
            id = game['appid']
            official_name = str(game['name'])

    if id == 1:
        return "Game not found."

    embed = ("https://store.steampowered.com/app/" + str(id))
    return embed

# TODO: Safety check for the case when there are multiple games with the same "game_name" variable
def SteamGameSearch(game_name):
    for game in steamJson["applist"]["apps"]:
        if game["name"].lower() == game_name.lower():
            id = game["appid"]
            embed = ("https://store.steampowered.com/app/" + str(id))
            try:
                return embed
            except:
                return "Game not found."

# Selects a random game from the whole steam library
def SelectRandomGame():   
    gameName = ""
    
    if gameName == "":
        maxValue = len(steamJson["applist"]["apps"]) # gets the object count of the json file
        randomValue = randint(0, maxValue)
        gameName = str(steamJson["applist"]["apps"][randomValue]["name"]) # gets the name of the specific game at the RandomValue value

    return gameName