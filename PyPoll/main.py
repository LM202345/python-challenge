# import the os module
import os

# module for reading csv files
import csv
path = os.getcwd()
csvpath = os.path.join(path,'Resources','election_data.csv')

with open(csvpath)as csvfile:
  # CSV reader specifies delimiter and variable that holds contents
  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvreader)
 
  # variable initialization
  counter=0
  # creation of a dictionary to store the names and votes of the candidates
  Candidates = dict ()

  # read each row of data after the header
  for row in csvreader:

    # total of votes
    counter= counter +1
    # read the name of the candidate
    namecandidate = str(row[2]) 

    # add the new candidate names to the dictionary and add up the votes for each candidate  
    if namecandidate in Candidates:
      Candidates [namecandidate] += 1
    else:
      Candidates [namecandidate] = 1
    
  # print the results in the terminal
  print("Election Results")  
  print("--------------------------------")
  print(f"Total Votes: {counter}")
  print("--------------------------------")

  before = 0
  for namecandidate, votes in Candidates.items():
    print(f"{namecandidate}: {(votes/counter)*100:.3f}% ({votes})")
    
    # identify who is the winner candidate
    if votes > before:
      Winner = namecandidate
    before = votes
  print("--------------------------------")
  print(f"Winner: {Winner}")
  print("--------------------------------")

  # export a text file with the results
  output_path = os.path.join (path,'analysis','PyPoll_results.txt')
  with open(output_path,'w') as txt:
    txt.write("Election Results\n")  
    txt.write("--------------------------------\n")
    txt.write(f"Total Votes: {counter}\n")
    txt.write("--------------------------------\n")
    for namecandidate, votes in Candidates.items():
      txt.write(f"{namecandidate}: {(votes/counter)*100:.3f}% ({votes})\n")
    txt.write("--------------------------------\n")
    txt.write(f"Winner: {Winner}\n")
    txt.write("--------------------------------\n")