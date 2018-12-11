# import pyodbc
import pymysql
import csv

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

def insert_records(table, yourcsv, cursor, cnxn):
    #INSERT SOURCE RECORDS TO DESTINATION
    with open(yourcsv) as csvfile:
        csvFile = csv.reader(csvfile, delimiter=',')
        header = next(csvFile)
        headers = map((lambda x: x.strip()), header)
        insert = 'INSERT INTO {} ('.format(table) + ', '.join(headers) + ') VALUES '
        for row in csvFile:
            values = map((lambda x: "'"+x.strip()+"'"), row)
            my_cursor.execute(insert +'('+ ', '.join(values) +');' )
            my_cnxn.commit() #must commit unless your sql database auto-commits

table = 'mydb.import'
mycsv = 'countries.csv' # SET YOUR FILEPATH
insert_records(table, mycsv, my_cursor, my_cnxn)
my_cursor.close()