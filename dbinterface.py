# -*- coding: utf-8 -*-
"""
Muhammad Aziz
March 5, 2020
"""


import sqlite3
#you need to run the sql file to intialize the db database and create the tables etc.

#this function takes the choices picked in the main method and creates queries using them
def queryEnter(numberOfChoices, sortSelection, sortOrder):
    
    #connects to 
    conn = sqlite3.connect('breakdowns.db')
    c = conn.cursor()
    
    query1 = "SELECT School_Year, Bus_ID, Bus_Company, Reason, Num_of_Students FROM breakdowns ORDER BY " + sortSelection + " " + sortOrder + " LIMIT " + str(numberOfChoices)
            
    query2 = "SELECT School_Year, Bus_ID, Bus_Company, Reason, Num_of_Students FROM breakdowns ORDER BY " + sortSelection + " " + sortOrder
    
    try:
        if (numberOfChoices == -1):
            c.execute(query2)
        else:
            c.execute(query1)
    except:
        print("Table(s) not found or could not be opened.")
    else:
        if (sortOrder == "ASC"):
            print('{:20} {:25} {:40} {:20} ({:4})'.format('School_Year','Bus_ID','Bus_Company','Reason','Num_of_Students'))
        for School_Year,Bus_ID, Bus_Company, Reason, Num_of_Students in c:
            print('{:20} {:25} {:40} {:20} ({:4})'.format(School_Year, Bus_ID,Bus_Company,Reason,Num_of_Students))
            
    # close the cursor 
    c.close()
    

def printingComponents():
    
    url = "https://data.cityofnewyork.us/Transportation/Bus-Breakdown-and-Delays/ez4e-fazm"
    print("This data was found using the following link: \n" + url)
    print()
    print("The data used in these records was from NYC Open Data where it shows information\n"+
          "collected from the Bus Breakdown and Delay system as of February 25,2020.\n The importance of this data is that"+ 
          "it demonstrates and pinpoints various bus companies, locations, and reasons of\n"+
          "why buses are delayed around NYC and some parts of the surrounding region.\n"+
          "Working with this data, the user can expect to add their own data points\n"+ 
          "aswell as search and perform their own data analysis on the data set.")
    print()

    
    
    
    
#Main Method
    
#variables
programContinue = True 
    
#initialization
printingComponents()
#sqlite_dataEntry()

#user input method
print()
#continues until user decides to quit
while (programContinue):
    
    #decides LIMIT (option 1)
    numberOfChoices = input("Enter a number for how many entries you would like to see or enter 'A' to see all: ")
    #decides SORT BY (option 2)
    sortSelection = input("Enter if you would like the sort to be by Borough (B), Number of Students (N), Bus Company (C) or School Year (Y): ").lower()
    #decides AESC or DESC (option 3)
    sortOrder = input("Would you like the sort to be (A)scending or (D)escending: ").lower()
    
    
    if (sortSelection == "b"):
        sortSelection = "Boro"
    elif (sortSelection == "n"):
        sortSelection = "Num_of_Students"
    elif (sortSelection == "c"):
        sortSelection = "Bus_Company"
    elif (sortSelection == "y"):
        sortSelection = "School_Year"
    else:
        print("Invalid selection for sort criteria, try again")
        continue;
    
    if (sortOrder == "d"):
        sortOrder = "DESC"
    else:
        sortOrder = "ASC"
        
    if (numberOfChoices.isnumeric()):
        queryEnter(numberOfChoices, sortSelection, sortOrder)
    else: 
        queryEnter(-1, sortSelection, sortOrder)
        
    flag = input("Would you like to continue searching? (Y/N): ").lower()
    if flag == "n":
        programContinue = False
        
        
    
