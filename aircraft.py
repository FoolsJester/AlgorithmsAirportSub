'''
Set of classes to store individual instances of aircrafts as well as dict store all aircrafts

I know in the specification it says that the aircraft was optional but I couldn't figure out a 
way to have either or. Right now I can only take inputs which have an aircraft specified

'''

import csv

class Aircraft:# stores individual classes of aircrafts
    model = ""
    manufacturer = ""
    distance = 0
    units = ""
    
    def __init__(self, model, manufacturer, distance, units):
        self.model = model
        self.manufacturer = manufacturer
        self.distance = distance
        self.units = units
    
class AircraftList(object): # class which stores all aircraft instances in dictionary by code
    aircraftDict= {}
    def __init__(self, filename):
        self.filename = filename
        
    def loadAircrafts(self):
        with open(self.filename, encoding="utf-8", newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                #checks to make sure all instances are unique
                if row[0] in AircraftList.aircraftDict:
                    print("The craft with code", row[0], "already exists in Aircraft. This duplicate will not be added")
                    continue
                else:    
                    # following determines if the distance is metric or not, if is metric just uses that value, if imperial converts to metric
                    if row[2] == 'metric':
                        self.aircraftDict[row[0]] = Aircraft(row[1], row[3], float(row[4]), row[2])
                    elif row[2] == 'imperial':
                        self.aircraftDict[row[0]] = Aircraft(row[1], row[3], float(row[4])*1.60934, row[2]+' converted')
    
    def getAircraft(self, code):
        return self.aircraftDict[code].model, self.aircraftDict[code].manufacturer, self.aircraftDict[code].distance, self.aircraftDict[code].units
                
 
    
inst = AircraftList('aircraft.csv')
inst.loadAircrafts()
