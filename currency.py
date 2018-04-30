import csv
'''
Creating instances of currencies and currency rates

We were told to combine these two data frames but I decided against it.
It is quite common that a currency exchange rate will change, but the 
currency of a country will rarely change. Therefore from a user standpoint
the currency rate csv will be regularly updated. If the files are combined
it means each country with currency X will need to be changed. My solution
uses the country file as a look up and is more user friendly if slightly less
efficient. 
'''
class Currency_Data: # Individual instance class for currency
    currency=""
    
    def __init__(self,  currency):
        self.currency = currency
        
class CurrencyList: # Class which contains dictionary of all country's currencies, agurment is filename
    currencyDict={}  
    def __init__(self,filename):
        self.filename = filename
    
    def loadCurrencyList(self): # takes self argument (filename) and extracts only relevant info - the country's currency
        with open(self.filename, encoding="utf-8", newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row[0] in CurrencyList.currencyDict: #checks to ensure "uniqueness" (sounds like a made-up word)
                    print("The country", row[0], "already exists. This duplicate will not be added")
                    continue
                else:
                    self.currencyDict[row[0]]= Currency_Data(row[14])
                    

    def getCountryCode(self, country): # returns the currency code of the supplied country
        return self.currencyDict[country].currency



class Currency_Rates:# class which provides the up to date currency exchange rate to euro, instance class
    rate = 0
    def __init__(self,rate):
        self.rate = rate
        
    
class RateList:# class stores all currency exchange rates to euro, takes filename as argument in main function
    rateDict = {} # stored in dictionary as acts like set, unordered and unique values only
    def __init__(self, filename): 
        self.filename = filename
    
    def loadCurrencyRate(self): # takes self instance (filename) and extracts relevant information- to euro exchange rate for each currency
        with open(self.filename, encoding="utf-8", newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row[1] in RateList.rateDict:
                    print("The currency with code", row[1], "already exists in Currency. This duplicate will not be added")
                    continue
                else:
                    self.rateDict[row[1]]= Currency_Rates(row[2])
                
                
    def getToEuroRate(self, code):# returns to euro exchange rate for the given currency code
        return self.rateDict[code].rate            
                
              
codes = CurrencyList('countrycurrency.csv')   
codes.loadCurrencyList()            

rates = RateList('currencyrates.csv')
rates.loadCurrencyRate()

    