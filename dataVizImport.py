# import pyodbc
import pymysql
import csv
import pandas as pd
from matplotlib import pyplot as plt
import os.path
# DESTINATION CONNECTION
# drivr = "ODBC Driver 13 for SQL Server"
# servr = "uao-nebula"
# db = "Staging"
# username = ""
# password = ""
# my_cnxn = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};'.format(drivr,servr,db))
# my_cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; SERVER=uao-nebula; DATABASE=Staging; Trusted_Connection=yes')

my_cnxn = pymysql.connect(host='localhost', port=3306, user='bkt5031', passwd='Phili467', db='mydb')
my_cursor = my_cnxn.cursor()


save_here = 'C:/Users/bkt5031/Desktop/dirPath'
filename = 'countries.csv'

r = 'r'
with open(filename, r) as file:     
    w = 'w'
    data = file.read()
    completeName = os.path.join(save_here, filename)
    file = open(completeName, w)
    file.write(data)
    # print (data)
    file.close()
    
# Compare the population growth in the US and China
data = pd.read_csv(filename) 
data.country == 'United States'

us = data[data.country == 'United States']
china = data[data.country == 'China']
print(us)
print(china)

print(us.population / us.population.iloc[0] * 100)

plt.plot(us.year, us.population / us.population.iloc[0] * 100, 'o')
plt.plot(china.year, china.population / china.population.iloc[0] * 100, 'o')
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()

def insert_records(table, yourcsv, cursor, cnxn):
    #INSERT SOURCE RECORDS TO DESTINATION
    with open(yourcsv) as csvfile:
        csvFile = csv.reader(csvfile, delimiter=',')
        header = next(csvFile)
        headers = map((lambda x: x.strip()), header)
        insert = 'INSERT INTO {} ('.format(table) + ', '.join(headers) + ') VALUES '
        for row in csvFile: 
            string_quote = "Cote d'Ivoire"
            newString    = string_quote.replace("Cote d'Ivoire", "Cote d Ivoire")
            values = map((lambda x: "'"+x.strip()+"'"), row)
            my_cursor.execute(insert +'('+ ', '.join(values) +');' )
            my_cnxn.commit() #must commit unless your sql database auto-commits

table = 'mydb.import'
mycsv = 'countries.csv' # SET YOUR FILEPATH
insert_records(table, mycsv, my_cursor, my_cnxn)
my_cursor.close()


