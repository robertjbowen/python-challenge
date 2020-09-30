"""
Created on Sat Sep 26 13:05:49 2020

@author: Robert Bowen
"""
import csv

# Path to collect data from the Resources folder
election_csv = 'Resources/election_data.csv'

total_votes = int(0)
most_votes = int(0)
winner_name = "The Voters"

# Dictionary to hold election results ["candidate name":, votes received]
vote_result = {}

# Read the csv file
with open(election_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

# read the header row in order to skip it
    csv_header = next(csv_file)

# iterate through each row in the data file
    for row in csv_reader:
        
# count the number of rows -> number of votes
        total_votes = total_votes + 1 

# Gather the candidate data from the data file row
        candidate = str(row[2])

# If the candidate is already in the dictionary, increment their vote count
        if candidate in vote_result:
            vote_result[candidate] += 1

# If the candidate is not in the dictionary, add them and give them 1 vote
        else:
            vote_result[candidate] = 1
    
# Create a text file in the Analysis directory, write the Election Result information to it, and Print the results to the terminal
f = open("Analysis/electionResults.txt", "w")        
f.write('Election Results\n\n')
f.write('-------------------------\n')
f.write(f'Total Votes: {total_votes}\n')
f.write('-------------------------\n')
print('\n\nElection Results\n')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

# For each candidate, calculate the percentage of the total vote, output the results, and check if they receved the most votes
for candidate_name in vote_result:
    can_votes = vote_result[candidate_name]
    per_votes = round(can_votes / total_votes *100,3)
    
    print(f'{candidate_name}: {per_votes}% ({can_votes})')
    f.write(f'{candidate_name}: {per_votes}% ({can_votes})\n')
    
    if can_votes > most_votes:
        most_votes = can_votes
        winner_name = candidate_name
        
f.write('-------------------------\n')
f.write(f'Winner: {winner_name}\n')
f.write('-------------------------\n')
f.close()
print('-------------------------')
print(f'Winner: {winner_name}')
print('-------------------------')

