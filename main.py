# this gonna be where all the files are, can all be loaded and ran from here
from Airports import *
from aircraft import *
from currency import *
from algorithm import *
import csv



def main():

    test_csv = Algorithm('test_cases.csv')
    test_csv.create_matrix()   
           
    
if __name__ == "__main__": main()
    