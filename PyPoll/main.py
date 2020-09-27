# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:05:49 2020

@author: Robert Bowen
"""
#import os
import csv

# Path to collect data from the Resources folder
election_csv = '/Users/RobandGrace/Documents/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv'

total_votes = int(-1)
winnerName = "The Voters"

def election_data(pollData):
    voter_id = int(pollData[0])
    County = str(pollData[1])
    Candidate = str(pollData[2])

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        total_votes = total_votes + 1
  
f = open("Analysis.txt", "w")        
f.write('Election Results\n\n')
f.write('-------------------------\n')
f.write(f'Total Votes: {total_votes}\n')
f.write('-------------------------\n')
# f.write(election results data here)
f.write('-------------------------\n')
f.write(f'Winner: {winnerName}\n')
f.write('-------------------------\n')
f.close()
 
print('\n\nElection Results\n')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
# print(election results data here)
print('-------------------------')
print(f'Winner: {winnerName}')
print('-------------------------')

