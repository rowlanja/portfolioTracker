from datetime import datetime, date
from coinbase.wallet.client import Client
import csv  



header = ['ticker', 'entry', 'currentPrice','sl','tp1', 'tp2', 'tp3', '% Gain', 'Profit', 'Datetime']
positions = []
coinbase_API_key = ""
coinbase_API_secret = ""

def updateCurrentPrice(position):
    ticker = position[0]
    date = date.today()
    client = Client(coinbase_API_key, coinbase_API_secret)
    price = client.get_spot_price(currency_pair= '-USD', date=date)  
    print(price)
    return position

def createPositions():
    finished = False
    while(not finished ):
        print("ADDING POSITION TO DATABASE")
        ticker = input("Ticker : ").upper()
        entry = input("Entry : ")
        sl = input("SL : ")
        tp1 = input("TP1 : ")
        tp2 = input("TP2 : ")
        tp3 = input("TP3 : ")
        time = datetime.now()
        gain = '--:-- %'
        profit = '$ ---.---'
        currentPrice = '$ ---.---'
        positions.add([ticker, entry, currentPrice, sl, tp1, tp2, tp3, gain, profit, time])
        if(input("Are you finished ? (y/n) : ") == 'y') : finished = True


def writePositions():
    with open('positions.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for entry in positions : 
            writer.writerow(entry)  

createPositions()
writePositions()