'''
Classes for storage of airport instances

First class stores individual instances of classes, second stores every airport in dictionary.
Second class also has load function, a get function, as well as 2 functions which allow the calculation
of the distance between 2 specified airports

'''

import csv
from math import pi,sin,cos,acos


class Airport:# class to store the individual instances of airport, names by 3 digit IATA code
    name = ""
    city = ""
    country = ""
    lat = 0
    lng = 0
    def __init__(self, name, city, country, lat, lng):
        self.name = name
        self.city = city
        self.country = country
        self.lat = lat
        self.lng = lng
        
    
    
class AirportAtlas(object):# class to store all airport instances in dictionary
    airportDict = {}
    def __init__(self,filename):# take filename as argument can be specified under function
        self.filename = filename
   
    def loadData(self): #file reading function which fills dict with instances of airports
        with open(self.filename, encoding="utf-8", newline='') as f:
            reader = csv.reader(f, delimiter=',')

            for row in reader:
                if row[4] in AirportAtlas.airportDict:
                    print("The airport with code",row[4],"already exists within Airports. This duplicate will not be added.")
                    continue
                else:
                    self.airportDict[row[4]] = Airport(row[1],row[2],row[3],row[6],row[7])
                
    def getAirport(self, code):
        return self.airportDict[code].name,self.airportDict[code].country, self.airportDict[code].lat, self.airportDict[code].lng
    
    @staticmethod
    def greatCircleDistance(latitude1, longitude1, latitude2, longitude2): # static method to calculate distance between 2 points given lat and long
        radius_earth = 6371 #km
        theta1 = float(longitude1) * (2 * pi) /360
        theta2 = float(longitude2) * (2 * pi) /360
        phi1 = (90 - float(latitude1)) * (2 * pi) /360
        phi2 = (90 - float(latitude2)) * (2 * pi) /360
        
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2)) * radius_earth
        
        return distance
    
    def distanceBetweenAirports(self, code1, code2):# function to assing the lats and longs of the tow airports, then passes to greatCircleDistance for distance
        
        lat1 = float(self.airportDict[code1].lat)
        lng1 = float(self.airportDict[code1].lng)
        lat2 = float(self.airportDict[code2].lat)
        lng2 = float(self.airportDict[code2].lng)
        
        return (AirportAtlas.greatCircleDistance(lat1, lng1, lat2, lng2))

    
a = AirportAtlas('airport.csv')
a.loadData()
 

