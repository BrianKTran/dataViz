# import pyodbc
import pymysql
import csv
import pandas as pd
from matplotlib import pyplot as plt
import os.path

save_plots = 'C:/Users/bkt5031/Downloads/my_folder/another_folder/dataViz/plotPics'
save_here  = 'C:/Users/bkt5031/Downloads/my_folder/another_folder/dataViz/output'
filename = 'C:/Users/bkt5031/Downloads/my_folder/another_folder/dataViz/input/countries.csv' # SET YOUR FILEPATH


def plotThis():
	

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

