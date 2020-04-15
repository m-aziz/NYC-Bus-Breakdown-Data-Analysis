#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:40:43 2020

@author: Aziz
"""


def file_prepare():
    print("Attempting to open file:")
    
    source_file = "Bus_Breakdown.csv" 
    output_file = "Bus_Breakdown_Cleaned.csv"
    lines_read,lines_written = 0,0
    
    try:
        data_in = open(source_file, 'r') 
    except: 
        print("the file could not be found")
        
    else:
        #the file opened
        data_out = open(output_file, 'w')
        count=0
        for line in data_in:
            lines_read +=1
            values = line.split(",")
            emptyElement = False

                
           
            #(5)This deletes rows with an empty element
            for i in range(0,8):
                if values[i]== "":
                    emptyElement = True
            if emptyElement == False: 
                new_line = ",".join(values)
                data_out.write(new_line)
                lines_written += 1
        
        #Closes Data input and output files
        data_in.close()
        data_out.close()
    
file_prepare()
