#!/usr/bin/python

import pandas as pd
from matplotlib import pyplot as plt
import os.path
import pyodbc
import pysftp
import urllib.parse

sql_conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=UAO-NEBULA; DATABASE=Staging; Authentication=SQL SERVER Authentication; Login=cfserver; Password=cf80767468; Trusted_Connection=yes') 
query = "SELECT * FROM [STAGING].[dbo].[TalismaLeadCards]"
# query = "insert into [STAGING].[dbo].TalismaLeadCards([first_name], [middle_initial], [last_name]) Values ('brian', 'k', 'tran');"
df = pd.read_sql(query, sql_conn)
print(df)
df.head(5)

save_here = 'C:/Users/bkt5031/Desktop/dirPath'

filename = 'C:/CommonApp/CommonApp_Prospect.txt'
# open(filename, mode='r')
r = 'r'

with open(filename, r) as file:  #  'r' is to read
	w = 'w'
	data = file.read()
	completeName = os.path.join(save_here, 'prospectCommApp.txt')
	file = open(completeName, w)
	file.write(data)
	# print (data)
	file.close()

# plt.plot(data.year, data.population)
