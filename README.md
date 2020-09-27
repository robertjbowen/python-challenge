# python-challenge

PyBank creates a Python script for analyzing financial records to determine:

1. Duration of Dataset
2. Total Profits
3. Average Monthly Change
4. Greatest Monthly Increase in profits - Gain (Date and Amount)
5. Greatest Monthly Decrease in profits - Loss (Date and Amount)

<<<<<<< HEAD
Input budget data is read from a .csv file located in the resources folder 
The script iterates through the budget data, counting the number of rows (months), and adding the gain/loss data to the total profits. 
The script then compares the monthly gain/loss data to a list holding the greatest monthly gain and loss values and their associated months of occurrance. If the gain/loss is greater, it updates the list with the new value and the month of occurance. 
=======
Input budget data is read from a .csv file located in the resources folder
The script iterates through the budget data, counting the number of rows (months), and adding the gain/loss data to the total profits. The script then compares the monthly gain/loss data to a list holding the greatest monthly gain and loss values and their associated months of occurrance. If the gain/loss is greater, it updates the list with the new value and the month of occurance.
>>>>>>> 37a27d5b2a9ff590cab336738d302b035ae9e137
Next, the script calulates the average monthly change and creates an output file called financialAnalysis.txt located in the Analysis folder where it writes a formatted table of results. 
Finally, the output analysis is printed to the terminal in the same format as the output file.

************************************************************************************************

PyPoll creates a Python script for analyzing voting results to determine:

1. Total votes cast
2. Complete list of candidates who received votes
3. Percentage of votes each candidate won
4. Total number of votes each candidate won
5. The winner of the election based on votes

Input budget data is read from a .csv file located in the resources folder 
The script iterates through the election data, counting the number of rows (votes)
The script then compares the candidate name to a dictionary of vote results. If the candidate is already in the list, it adds one vote to the vote talley. If not in the dictionary, the candidate is added and given one vote.
Next, the percent of the total vote won is computed for each candidate and total votes are compared to determine the winner
Finally, The output analysis is printed to the terminal and exported to a text file called electionResults.txt located in the Analysis folder.

************************************************************************************************

