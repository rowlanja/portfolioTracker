from datetime import datetime, date
import os
import csv
from binance.client import Client
  
class Position:
    def __init__(self, ticker, entry, size, exit, lvs, margin):
        self.ticker = ticker
        self.entry = entry
        self.size = size
        self.exit = exit
        self.lvs = lvs
        self.margin = margin
        self.gain = '--:-- %'
        self.profit = '$ ---.---'
        self.currentPrice = '$ ---.---'
        self.dateTime = '--/--/--'

    def getTicker(self):
        return self.ticker
    def setTicker(self, x):
        self.ticker = x

    def getEntry(self):
        return self.entry
    def setEntry(self, x):
        self.entry = x

    def getSize(self):
        return self.size
    def setSize(self, x):
        self.size = x

    def getExit(self):
        return self.exit
    def setExit(self, x):
        self.exit = x

    def getLVS(self):
        return self.lvs
    def setLVS(self, x):
        self.lvs = x

    def getGain(self):
        return self.gain
    def setGain(self, x):
        self.gain = x

    def getProfit(self):
        return self.profit
    def setProfit(self, x):
        self.profit = x

    def getCurrentPrice(self):
        return self.currentPrice
    def setCurrentPrice(self, x):
        self.currentPrice = x

    def getMargin(self):
        return self.margin
    def setCurrentMargin(self, x):
        self.margin = x

    def getDatetime(self):
        return self.dateTime
    def setDatetime(self, x):
        self.dateTime = x

    def toArr(self):
        return [
            self.ticker,
            self.entry,
            self.size,
            self.margin,
            self.exit,
            self.gain,
            self.profit,
            self.dateTime,
            self.ticker,
            self.lvs
        ]
    
header = ['Ticker', 'Entry','Size (ticker)','Margin (usd)','Exit', '% Gain', 'Profit', 'Datetime', 'Long or Short']
newPositions = []
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

def updateCurrentPrice(position):
    ticker = position.getTicker()
    client = Client(api_key, api_secret)
    currentPrice = client.get_symbol_ticker(symbol=ticker+"USDT")
    dollarDifference = (position.getSize() * float(currentPrice["price"])) - (position.getSize() * float(position.getEntry()))
    position.setProfit(dollarDifference)
    position.setGain(str(round(dollarDifference/position.getMargin(),5)*100) + "%")
    position.setDatetime(datetime.now())
    print(currentPrice["price"])
    print('$ gain', position.getGain())
    print('$ profit', position.getProfit())
    return position

def createPositions():
    finished = False
    while(not finished ):
        print("ADDING POSITION TO DATABASE")
        ticker = input("Ticker : ").upper()
        entry = float(input("Entry : "))
        size = float(input("Size (ticker) : "))
        margin = int(input("Margin : "))
        exit = float(input("Exit : "))
        lvs = input("Long or Short?(l/s) : ")
        position = Position(ticker, entry, size, exit, lvs, margin)
        updateCurrentPrice(position)
        newPositions.append(position)
        if(input("Are you finished ? (y/n) : ") == 'y') : finished = True


def writePositions():
    with open('positions.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for position in newPositions : 
            position = position.toArr()    
            writer.writerow(position)  

createPositions()
writePositions()