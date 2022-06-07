# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 16:02:03 2022

@author: ankit computer
"""
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("Tuples")
monthlabel = Label(root)

month = ("January","February","March","April","May","June","July","August","September","October","November","December")
profits = (2000,3000,4550,2135,9431,103567,13456,32124,2457,21245,134576,99999)
max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month = month(max_profit_index)
print("The maximum profit of "+str(max_profit)+"Was recoreded in "+ str(max_profit_month))

min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = month(min_profit_index)
print("The minimum profit of "+str(min_profit)+"Was recoreded in "+ str(min_profit_month))
