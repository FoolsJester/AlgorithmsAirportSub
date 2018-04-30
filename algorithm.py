'''
Main algorithm of the project, takes a file containing potential journeys and finds route via greedy algorithm

Algorithm takes in argument of filename (file of potential trips) and creates a weighted graph of each of the 
airports giving the distances between them. This is a bidirectional weighted graph due to the exchange rates.
Both distance and cost is stored in this graph for simplicity. Cost is the main attribute defining the vertices. 
The distance is included to ensure the specified aircraft can make the distance.

Returns to "main" function with potential route and cost or saying that the journey cannot be made with the specfied 
aircraft.

If errors are present they will be printed to the console, output is in results.csv
'''

from Airports import *
from currency import  *
from aircraft import *
import math

class Algorithm: # algorithm class used to store bi-weighted graph and call the greedy algorithm
    matrix = {}
    def __init__(self,filename):
        self.filename = filename
    
    
    #following is the function which created the weighted graph. Takes input of self(filename) and stores in dictionary
    #structure of the dictionary is the-- starting airport: {potential next airport: distance, cost} repeated     
    def create_matrix(self):
        with open('test_cases.csv', encoding="utf-8", newline='') as f:
            reader = csv.reader(f, delimiter=',')
            
            for row in reader:
                count1 = 0 #count is here because don't want to include the provided aircraft as an airport
                for air1 in row: # air1 is the starting airport
                    cost_matrix= {}
                    self.country = a.getAirport(air1)[1] #country needed for currency
                    self.code1= air1
                    
                    
                    count2 = 0
                    for air2 in row:# air 2 is the potential destination airport
                        if air1 == air2:# if 2 airports are same no need for computation of distance
                            count2+=1
                            continue
                        if air1 in Algorithm.matrix: # checks to see if starting airport is already in matrix
                            if air2 in air1:#checks to see if potential destination airport is already in dict for starting airport
                                count2+=1
                                continue
                            
                        self.code2 = air2                    
                        
                        #takes the two airport codes and passes them to distance between airports, which passes relevant lat lng to great circle dist
                        distance = a.distanceBetweenAirports(self.code1, self.code2)
                        
                        country_currency = codes.currencyDict[self.country].currency # gets country's currency
                        to_euro_rate = rates.getToEuroRate(country_currency)# gets currency rate
                        cost_matrix.update({air2:[distance,distance*float(to_euro_rate)]}) #converts distance to a cost in euros 
                        count2 +=1
                        
                        
                        if count2 >= len(row)-2: #breaks before encounters cell containing aircraft
                            break
                        
                        
                    Algorithm.matrix.update({air1:cost_matrix})  #updates the graph with the starting airport and all other potential airports
                    count1 +=1
    
                    if count1 >= len(row)-1: #break to ensure doesn't take aircraft as airport
                        break
        
                output = Algorithm.greedy(row)
                with open('results.csv', 'a') as file:
                    wr = csv.writer(file, dialect = 'excel')
                    wr.writerow(output)
            
    #static method to calculate a potential route using a greedy algorithm
    @staticmethod   
    def greedy(airports): # greedy algorithm which takes a row from csv as argument
        itinerary=[] # this is eventual itinerary
        home = airports[0] # defining the home airport, will be first and last in itinerary
        craft_details = inst.getAircraft(airports[len(airports)-1]) # get information of supplied aircraft
        itinerary.append(home)
        total_cost = 0
    
         
        for i in range(0,len(airports)-2): #range for airports, excluding aircraft
            key = itinerary[len(itinerary)-2] # key will always be last entry into intinerary
    
            dist_dict = Algorithm.matrix.get(key) #getting the dictionary of distances for the next airport in itinerary
    
            
            
            cost = math.inf # assign infinity to cost, therefore everything must be lower
            next_stop = ""
            for key1, value in dist_dict.items():
                if value[0]> float(craft_details[2]): #if value is greater than possible distance, skip loop
                    continue
                elif float(value[1])<=cost and key1 not in itinerary: #this will change current cost and next dest IF possible to travel and not in itinierary already
                    cost = float(value[1])
                    next_stop = key1
                else: #this is basically here to prevent duplicate entries into the route other than home
                    continue
                 
                 
            if next_stop == "": #if no next airport found due to distance too great this command will break from loop
                break
            else:
                itinerary.append(next_stop)
                total_cost+=cost

               
        if len(itinerary) < len(airports)-1: #if the amount of airports in itinerary is not sufficient, means one leg too long therefore return error
            return airports, "No valid path for this selection of airports. Ensure no duplicates and specified plane capable of making journey"
        
        elif Algorithm.matrix[itinerary[len(itinerary)-1]][home][0]>= craft_details[2]:#if aircraft incapable of making final leg of journey to home airport = error
            return airports,"This aircraft cannot make final leg of journey"
        
        elif Algorithm.matrix[itinerary[len(itinerary)-1]][home][0]<= craft_details[2]:#if home journey possible, append to itinerary
            total_cost += Algorithm.matrix[itinerary[len(itinerary)-1]][home][1]
            itinerary.append(home)
        
        return itinerary, total_cost #returns the itinerary and the total cost of the flights