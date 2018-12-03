#!/usr/bin/python

import pandas as pd
from matplotlib import pyplot as plt




data = pd.read_csv('countries.csv')

# Compare the population growth in the US and China
 
data.country == 'United States'

us = data[data.country == 'United States']
china = data[data.country == 'China']
# print(us)
# print(china)

print(us.population / us.population.iloc[0] * 100)

plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()

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