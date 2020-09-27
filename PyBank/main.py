# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:05:49 2020

@author: Robert Bowen
"""
import csv

# Path to collect data from the Resources folder
budget_csv = 'Resources/budget_data.csv'

total_months = int(-1)

def budget_data(budgetData):
    month = str(budgetData[0])
    profit = int(budgetData[1])
    
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        total_months = total_months + 1
  
f = open("Analysis/financialAnalysis.txt", "w")        
f.write('Financial Analysis\n\n')
f.write('-------------------------\n')
f.write(f'Total Months: {total_months}\n')
f.write('-------------------------\n')
# f.write(financial analysis data here)
f.close()
 
print('\n\nFinancial Analysis\n')
print('-------------------------')
print(f'Total Months: {total_months}')
print('-------------------------')
# print(financial analysis data here)

