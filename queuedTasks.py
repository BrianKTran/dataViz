#!/usr/bin/python

import pandas as pd
from matplotlib import pyplot as plt
import os.path
# import pysftp

save_here = 'C:/Users/bkt5031/Desktop/dirPath'

filename = 'queuedTasks.csv'
# open(filename, mode='r')
r = 'r'

with open(filename, r) as file:  #  'r' is to read
	w = 'w'
	data = file.read()
	completeName = os.path.join(save_here, 'newQueuedTasks.csv')
	file = open(completeName, w)
	file.write(data)
	# print (data)
	file.close()

# plt.plot(data.year, data.population)
