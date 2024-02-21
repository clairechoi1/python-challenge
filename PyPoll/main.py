#import modules 
import os
import csv

counter_dict={}
csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header row
    next(csvreader)

    #initialize variables
    total_votes=0

    #Loop through each row in CSV file
    for row in csvreader:
        total_votes+=1
        name=row[2]
        if name in counter_dict:
            counter_dict[name]=counter_dict[name]+1
        else:
            counter_dict[name]=1
        
        winner=max(counter_dict, key=counter_dict.get)


print("Election Results")
print("-------------------------")
#The total number of votes cast
print(f"Total Votes: {total_votes}")
print("-------------------------")
#A complete list of candidates who received votes
for candidate, votes in counter_dict.items():
#The percentage of votes, and total number of votes each candidate won
    percentage=(votes/total_votes)*100
    print(f"{candidate}:{percentage:.3f}%({votes})")
print("-------------------------")
#The winner of the election based on popular vote
print(f"Winner:{winner}")
print("-------------------------")

#Export analysis to a text file
output_path = os.path.join("..","PyPoll","analysis", "pypoll_results.txt")
with open(output_path, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
   
    for candidate, votes in counter_dict.items():
        percentage=(votes/total_votes)*100
        file.write(f"{candidate}:{percentage:.3f}%({votes})\n")

    file.write("-------------------------\n")
    file.write(f"Winner:{winner}\n")
    file.write("-------------------------\n")