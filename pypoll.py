import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 initialize a total voter counter
total_votes = 0

#candidate options
candidate_options = []

#candidate options and candidate votes
candidate_options = []

#1 declare the empty dictionary
candidate_votes = {}

#open the election results and read teh file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1

        #print the candiate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            #add the candidate name to the list
            candidate_options.append(candidate_name)

            #2 begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidates count
        candidate_votes[candidate_name] +=1
        #determing the winning vote count and candidate
        # 1. determine if the cotes are greater than the winning count

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #2 if true then set winning_count = votes and winning_percentage = 
                #vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #3 set the winning candidate = candidate name
                # winning_candidate = candidate_name
#print the candidate vote dictionary
print(candidate_votes)

#determing the percentage of votes for each candidate by looping thorugh the counts
#1 iterate through the candidate list
for candidate_name in candidate_votes:
    #2 retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3 calculate % of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #to do: print oout each candidates name, vote count, and percentage of
    #votes to the terminal

    #determing winning and vote count and candidates
    #determing if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if ture then set winning count = votes and winning percentage as vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #and set winning candidate = candidate name
        winning_candidate = candidate_name
    #4 print the results
    print(f"{candidate_name} : received {vote_percentage}% of the vote.")

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    for row in file_reader:
        #2 Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)
