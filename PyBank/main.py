# import the os module
import os
 # module for reading csv files

import csv
path = os.getcwd()

csvpath = os.path.join(path,'Resources','budget_data.csv')

with open(csvpath)as csvfile:

# CSV reader specifies delimiter and variable that holds contents

  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvreader)
 
 
# variable initialization

  counter=0
  totalProfitLosses = 0
  totalchange = 0
  greatestincrease = 0
  greatestdecrease = 0

  # read each row of data after the header
  for row in csvreader:

    # totals the number of periods analyzed
    counter= counter +1

    # accumulate profit and losses 
    totalProfitLosses = totalProfitLosses + int(row[1])
    # Starting at row 2, calculate the change in "Profit/Losses 
    if counter > 1:
      change = int(row[1])- lastmonthprofit 
      # accumulates the changes to obtain the average change at the end
      totalchange = change + totalchange 
      # detects the greatest increment and save the date
      if greatestincrease < change:
              greatestincrease = change
              greatestincreasedate = row [0]
      # detects the greatest decrement and save the date        
      if greatestdecrease > change:
              greatestdecrease = change
              greatestdecreasedate = row [0]          

    # stores the value of the profit to be able to compare it with the next period
    lastmonthprofit = int(row[1])
      
  
  # print the results in the terminal
  print("Financial Analysis")  
  print("--------------------------------")
  print(f"Total Months: {counter}")
  print(f"Total: ${totalProfitLosses}")
  print(f"Average Change: ${totalchange/(counter-1):.2f}")
  print(f"Greatest Increase in Profits: {greatestincreasedate} (${greatestincrease})")
  print(f"Greatest Decrease in Profits: {greatestdecreasedate} (${greatestdecrease})")

  # export a text file with the results
  output_path = os.path.join (path,'analysis','PyBank_results.txt')
  with open(output_path,'w') as txt:
  
    txt.write("Financial Analysis\n")  
    txt.write("--------------------------------\n")
    txt.write(f"Total Months: {counter}\n")
    txt.write(f"Total: ${totalProfitLosses}\n")
    txt.write(f"Average Change: ${totalchange/(counter-1):.2f}\n")
    txt.write(f"Greatest Increase in Profits: {greatestincreasedate} (${greatestincrease})\n")
    txt.write(f"Greatest Decrease in Profits: {greatestdecreasedate} (${greatestdecrease})\n")






                       