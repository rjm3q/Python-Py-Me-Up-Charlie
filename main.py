# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:26:05 2019

@author: rober
"""

import os
import csv
currentDir = os.getcwd()
path = os.path.join('budget_data.csv')
months = []
avglist = []
avgchange = []
with open(path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        avglist.append(int(row[1]))
#average of changes in profit/loss
    total = sum(avglist)
#greatest increase in profit
    for loss in avglist:
        if loss == avglist[0]:
            last = loss
        else:
            new = loss - last
            avgchange.append(new)
            last = loss

    avg = sum(avgchange) / (len(months)-1)
#greatest decrease in loss
    incr = avgchange.index(max(avgchange))
    decr = avgchange.index(min(avgchange))




print ("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(len(months)))
print("Total: $" + str(total))
print("Averagre Change: " + str(avg))
print("Greatest Increase: " + str(incr))
print("Greatest Decreas: " + str(decr))