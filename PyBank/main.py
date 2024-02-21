
#import modules 
import os
import csv

csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header row
    next(csvreader)
    
    # Initialize variables
    total_months = 0
    net_total = 0
    changes = []
    dates = [] 

    #Loop through each row in CSV file
    for row in csvreader:
        date= row[0]
        profit_losses=int(row[1])
        #add total number of months
        total_months+=1
        #calculate net total
        net_total+=profit_losses
        #store values
        dates.append(date)
        changes.append(profit_losses)

    #calculate changes in profit and loss
    change_values= [changes[i+1] - changes[i] for i in range(len(changes) - 1)]
    #calculate average change 
    avg_change=sum(change_values) / len(change_values)
    #locate greatest increase and decrease in profits
    max_increase=max(change_values)
    max_decrease=min(change_values)
    #dates for the greatest increase and decrease in profits
    max_increase_date = dates[change_values.index(max_increase) + 1]
    max_decrease_date = dates[change_values.index(max_decrease) + 1]

    #Print results
    print("Financial Analysis")
    print("----------------------------")
    #The total number of months included in the dataset
    print(f"Total Months: {total_months}")
    #The net total amount of "Profit/Losses" over the entire period
    print(f"Total: ${net_total}")
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    print(f"Average Change: ${avg_change:.2f}")
    #The greatest increase in profits (date and amount) over the entire period
    print(f"Greatest Increase in Profits: {max_increase_date}(${max_increase})")
    #The greatest decrease in profits (date and amount) over the entire period
    print(f"Greatest Decrease in Profits: {max_decrease_date}(${max_decrease})")

    #Export analysis to a text file
    output_path = os.path.join("..","PyBank","analysis", "pybank_results.txt")
    with open(output_path, "w") as file:
        file.write("Financial Analysis\n")
        file.write("----------------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${net_total}\n")
        file.write(f"Average Change: ${avg_change:.2f}\n")
        file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
        file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")
