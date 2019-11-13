# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:26:05 2019

@author: rober
"""

import os
import csv

#setfilepath
csvpath= os.path.join("budget_data.csv")

#lists
months= []
profits_losses= []
changes= []

#opens the csv file to read
with open(csvpath, newline='', encoding='utf8') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")
    csv_header = next(csvreader)

    #populate lists
    for row in csvreader:
        months.append(row[0])
        profits_losses.append(int(row[1]))

    total = sum(profits_losses)

    #calculates change by month
    for prof_loss in profits_losses:
        if prof_loss == profits_losses[0]:
            previous= prof_loss
        else:
            change= prof_loss - previous
            changes.append(change)
            previous= prof_loss

    #assigns variables for printing
    average= sum(changes) / (len(months)-1)
    greatest_increase_index= changes.index(max(changes))
    greatest_decrease_index= changes.index(min(changes))

#output
print(f"""
-----------------
Financial Data
-----------------
Total Number of Months: {len(months)}
Total Profits/Losses: ${total}
Average Change: ${round(average,2)}
Greatest Increase: {months[greatest_increase_index + 1]} (${changes[greatest_increase_index]})
Greatest Decrease: {months[greatest_decrease_index +1]} (${changes[greatest_decrease_index]})
""")

output_file= os.path.join("PyBank_output.txt")

output= open(output_file, "w")
output.write(f"""
-----------------
Financial Data
-----------------
Total Number of Months: {len(months)}
Total Profits/Losses: ${total}
Average Change: ${round(average,2)}
Greatest Increase: {months[greatest_increase_index + 1]} (${changes[greatest_increase_index]})
Greatest Decrease: {months[greatest_decrease_index +1]} (${changes[greatest_decrease_index]})