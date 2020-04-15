/* Homework 4 Assignment 
Muhammad Aziz
ma5264*/



/* Bus Breakdowns and Delayed Incidents
This data is a data set that I found regarding Bus Breakdowns and Delays on February 25, 2020
SOURCE
https://data.cityofnewyork.us/Transportation/Bus-Breakdown-and-Delays/ez4e-fazm
*/


DROP TABLE IF EXISTS 'breakdowns';
CREATE TABLE IF NOT EXISTS 'breakdowns' (
  "School_Year" TEXT,
  "Bus_ID" TEXT,
  "Run_Type" TEXT,
  "Reason" TEXT,
  "Boro" TEXT,
  "Bus_Company" TEXT,
  "Num_of_Students" INTEGER,
  "School_Notified" TEXT,
  "Parent_Notified" TEXT

);

.mode csv
.import Bus_Breakdowns.csv breakdowns
.mode columns
.width 40

