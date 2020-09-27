"""
Created on Sat Sep 26 13:05:49 2020

@author: Robert Bowen
"""
import csv

# Path to collect data file from the Resources folder
budget_csv = 'Resources/budget_data.csv'

# Initialize variables
total_months = int(0)
total_profit = int(0)

# List to hold budget data [month of greatest gain, value greatest gain, month of greatest loss, value greatest loss]
hi_lo = ['a',0,'b',0]

# Read the csv file
with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

# read the header row in order to skip it
    csv_header = next(csv_file)

# iterate through each row in the data file
    for row in csv_reader:
        
# count the number of rows -> number of months
        total_months = total_months + 1 

# Gather the date and gain/loss data from the data file row
        month = str(row[0])
        profit = int(row[1])
        
# Add the profit from the row to the total profit        
        total_profit = total_profit + profit

# Compare the gain/loss info to the current values for greatest gain or loss -> if greater update list with new value and date
        if profit > hi_lo[1]:
            hi_lo[0] = month
            hi_lo[1] = profit
        elif profit < hi_lo[3]:
            hi_lo[2] = month  
            hi_lo[3] = profit
 
# Calculate the average change
    average_change = round(total_profit / total_months,2)    
 
# Create a text file in the Analysis directory and write the Financial Analysis information to it        
f = open("Analysis/financialAnalysis.txt", "w")        
f.write('Financial Analysis\n\n')
f.write('-------------------------\n')
f.write(f'Total Months: {total_months}\n')
f.write(f'Total: ${total_profit}\n')
f.write(f'Average Change: ${average_change}\n')
f.write(f'Greatest Increase in Profits: {hi_lo[0]} (${hi_lo[1]})\n')
f.write(f'Greatest Decrease in Profits: {hi_lo[2]} (${hi_lo[3]})\n')
f.write('-------------------------\n')
f.close()

# Print the Financial Analysis information to the terminal  
print('\n\nFinancial Analysis\n')
print('-------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {hi_lo[0]} (${hi_lo[1]})')
print(f'Greatest Decrease in Profits: {hi_lo[2]} (${hi_lo[3]})')
print('-------------------------')
