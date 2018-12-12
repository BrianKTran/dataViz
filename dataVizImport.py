# import pyodbc
import pymysql
import csv
import pandas as pd
from matplotlib import pyplot as plt
import os.path
import plot as pt
import wnCsv

# DESTINATION CONNECTION

my_cnxn = pymysql.connect(host='localhost', port=3306, user='bkt5031', passwd='Phili467', db='mydb')
my_cursor = my_cnxn.cursor()
save_here = 'C:/Users/bkt5031/Desktop/dirPath'

pt.plotThis()

def insert_records(table, yourcsv, cursor, cnxn):
    #INSERT SOURCE RECORDS TO DESTINATION
    with open(yourcsv) as csvfile:
        csvFile = csv.reader(csvfile, delimiter=',')
        header = next(csvFile)
        headers = map((lambda x: x.strip()), header)
        insert = 'INSERT INTO {} ('.format(table) + ', '.join(headers) + ') VALUES '
         
         # print (data)
          
        for row in csvFile: 
            
            values = map((lambda x: "'"+x.strip()+"'"), row)
            my_cursor.execute(insert +'('+ ', '.join(values) +');' )
            my_cnxn.commit() #must commit unless your sql database auto-commits
         
table = 'mydb.import'
mycsv = 'C:/Users/bkt5031/Downloads/my_folder/another_folder/dataViz/input/countries.csv' # SET YOUR FILEPATH
insert_records(table, mycsv, my_cursor, my_cnxn)
wnCsv.writeNewCsv(mycsv)
my_cursor.close()

# string_quote = "Cote d'Ivoire"
# newString    = string_quote.replace("Cote d'Ivoire", "Cote d Ivoire")