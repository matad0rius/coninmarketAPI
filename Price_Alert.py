import json
import time
import pandas as pd
import pyttsx3
import requests

data_frame = pd.read_csv('Coins.csv'),
                        usecols = ['Symbol', 'Up', 'Down'])

data_frame = data_frame.to_json()
data_frame = json.loads(data_frame)

symbols = data_frame['Symbols']
up_limits = data_frame['Up']
down_limits = data_frame['Down']

symbols = [symbols[x] for x in symbols]

print(symbols)

up_limits = [100000 if float(up_limits[x]) is None else for x in symbols]
down_limits = [0 if float(down_limits[x]) is None else for x in symbols]

current_price = [0 for x in range(len(symbols))]
symbols_id  = [0 for x in range(len(symbols))]

api = 'https://api.coinmarketcap.com/v2/listings/'
data = requests.get.(api).json()['data']

for currency in data:
    if currency['name'] in symbols:
        symbols_id[symbols.index(currency['name'])] = currency['id']
        
api = 'https://api.coinmarketcap.com/v2/ticker/'

engine = pyttsx3.init() # computer.speak

def printing():
    while True:
        for index in range(len(symbols)):
            temp_api = api + str(symbols_id[index])
            data =  requests.get(temp_api).json()
            current_price[index] = float(data['data']['quotes']['USD']['price'])
            
            if current_price[index] > up_limit[index]:
                speak("%-10s price is %.2f" % (symbols[index], current_price[index])
            if current_price[index] < down_limit[index]:
                speak("%-10s price dropped %.2f" % (symbols[index], current_price[index])
                
            time.sleep(300)

def speak(msg):
    print(msg)
    engine.say(msg)
    engine.runAndWait()
 
 
# create a csv file (Coins.csv)
    # Symbol, Up, Down
    # Bitcoin, 5000, 6000

# create text file (Price_alet.bat) with extension .bat
    # py -3 destination of your file install # version of python 
    
    
# create a new file (run_in_bg.vbs) extension .vbs # to run in background
    # Set oShell = CreateObject ("Wscript.Shell")
    # Dim strArgs
    # strAgs = "cmd /c Price_alert.bat"
    # oShell.Run strAgs, 0, false
    
    




