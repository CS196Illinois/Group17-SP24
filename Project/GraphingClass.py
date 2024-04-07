import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Designed to take in multiple particle df, and then
# create a graph off of data.
# eventually will implement having animations
#
class Graphing:
    def __init__(self):
        # eventually can control window parameters
        #fig = plt.figure()
        fig, axs = plt.subplots()


    def set_xlim(self, lower : float, upper : float):
        plt.xlim(lower,upper)
    def set_ylim(self, lower : float, upper : float):
        plt.ylim(lower,upper)

    # assumes DataFrame comes in with following form:
    # X_pos: col 0, Y_pos: col 1
    def add_df(self,df :pd.DataFrame):
        x_list = df.iloc[:,[0]]
        y_list = df.iloc[:,[1]]
        
        plt.plot(x_list, y_list, 'o')

    def show(self):
        plt.show()