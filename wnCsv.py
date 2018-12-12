import pymysql
import csv
import pandas as pd
from matplotlib import pyplot as plt
import os.path


save_here = 'C:/Users/bkt5031/Downloads/my_folder/another_folder/dataViz/output'
targetCsv = 'C:/Users/bkt5031/Downloads/my_folder/another_folder/dataViz/input/countries.csv' # SET YOUR FILEPATH

def writeNewCsv(targetCsv):
    with open(targetCsv) as csvfile:
        data = csvfile.read()
        completeName = os.path.join(save_here, 'newCountries.csv')
        csvfile = open(completeName, 'w')
        csvfile.write(data)
        csvfile.close()