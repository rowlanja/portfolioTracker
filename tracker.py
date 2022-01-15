from datetime import datetime
import csv  
import requests


header = ['ticker', 'entry', 'sl','tp1', 'tp2', 'tp3', '% Gain', 'Profit', 'Datetime']
positions = []
coinbase_API_Key = ""
coinbase_API_Secret = ""

def updateCurrentPrice(position):
    ticker = position[0]
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        print(response.json())
        print(ticker + ' price updated')
    elif response.status_code == 404:
        print(ticker + 'Ticker Price Not Found.')
    return position

def createPositions():
    finished = False
    while(not finished ):
        print("ADDING POSITION TO DATABASE")
        ticker = input("Ticker : ").lower()
        entry = input("Entry : ")
        sl = input("SL : ")
        tp1 = input("TP1 : ")
        tp2 = input("TP2 : ")
        tp3 = input("TP3 : ")
        time = datetime.now()
        gain = '--:-- %'
        profit = '$ ---.---'
        positions.add([ticker, entry, sl, tp1, tp2, tp3, gain, profit, time])
        if(input("Are you finished ? (y/n) : ") == 'y') : finished = True


def writePositions():
    with open('positions.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for entry in positions : 
            writer.writerow(entry)  

createPositions()
writePositions()