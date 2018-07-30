import os
import csv

file = os.path.join("election_data.csv")
fileout = "Election_Results.txt"

with open(file,"r", newline="") as filename:
    csv=csv.reader(filename, delimiter=",")

    #Remove first row of text from rows and create empty lists for voters and candidates
    header = next(csv, None)
    votes=[]
    candidates=[]
    
    #Append the lists with relevant data then create a new list of the unique values for candidates
    for row in csv:
        votes.append(row[0])
        candidates.append(row[2])
    cand_list=set(candidates)
    
    #Calculate total number of votes by counting id's in votes list
    total = len(votes)
    
    #Create empty dictionary for determining winner and list for holding statement for each candidate's results
    final_results=[]
    win=0
    
    #Loop through to fill the dictionary with (candidate, percentage) key:values and create a variable for the candidates' results
    for candidate in cand_list:
        vote_count = candidates.count(candidate)
        popularity = vote_count/total * 100
        final_results.append(candidate + ": " + str(round(popularity,0)) + "% (" + str(vote_count) + ")")

        #Determine max value and assign winning value and winning candidate
        if popularity> win:
            win=popularity
            winningC=candidate

    #This variable will style the list printout of the overall results
    printout=('\n'.join(final_results))

    #Create one single variable to send to the txt file that will print all of the info needed
    election_results = (f"Election Results: \n" 
    f"-----------------------\n"
    f"Total votes: {total}\n"
    f"-----------------------\n"
    f"{printout}\n"
    f"-----------------------\n"
    f"The winner is: {winningC}\n"
    f"-----------------------")

    print(election_results)

#Write to txt file
with open(fileout, "w") as txt_file:
    txt_file.write(election_results)