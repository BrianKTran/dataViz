#!/usr/bin/python
# import pymssql
import pymysql
import pandas as pd
from matplotlib import pyplot as plt
import os.path


conn = pymysql.connect(host='localhost', port=3306, user='bkt5031', passwd='Phili467', db='mydb')

cur = conn.cursor()

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

cur.execute("SELECT * FROM import")

print(cur)
conn.close()

# x = [1, 2, 3] 
# y = [1, 4, 9]
# z = [10, 5, 0]


# plt.plot(x, y)  
# plt.plot(x, z)
# plt.title("test plot")
# plt.xlabel("x")
# plt.ylabel("y and z")
# plt.legend(["this is y", "this is z"])

# sample_data = pd.read_csv('sample_data.csv')
# plt.plot(sample_data.column_a, sample_data.column_b)
# plt.plot(sample_data.column_a, sample_data.column_c)
# print(type(sample_data))
# print(sample_data)

# print(type(sample_data.column_c))
# print(sample_data.column_c)

# print(type(sample_data.column_c.iloc[0]))
# print(sample_data.column_c.iloc[0])
# print(sample_data "\n"
# 	  sample_data.column_c.iloc[1] "\n"  
# 	  sample_data.column_c "\n" 
# 	  type(sample_data) "\n"
# 	  type(sample_data.column_c) "\n"
# 	  type(sample_data.column_c.iloc[1])
# 	)