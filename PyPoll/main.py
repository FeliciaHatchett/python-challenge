import os
import csv

file = os.path.join("election_data.csv")
fileout = "Election_Results.txt"

with open(file,"r", newline="") as filename:
    csv=csv.reader(filename, delimiter=",")

    header = next(csv, None)
    votes=[]
    candidates=[]
    for row in csv:
        votes.append(row[0])
        candidates.append(row[2])
    cand_list=set(candidates)
    
    total = len(votes)
    candict={}
    final_results=[]
    win=0
    for candidate in cand_list:
        vote_count = candidates.count(candidate)
        popularity = vote_count/total * 100
        candict[candidate]=vote_count
        final_results.append(candidate + ": " + str(round(popularity,0)) + "% (" + str(vote_count) + ")")

        if popularity> win:
            win=popularity
            winningC=candidate

        
    printout=('\n'.join(final_results))

    election_results = (f"\nElection Results: \n" 
    f"-----------------------\n"
    f"Total votes: {total}\n"
    f"-----------------------\n"
    f"{printout}\n"
    f"-----------------------\n"
    f"The winner is: {winningC}\n"
    f"-----------------------")

    print(election_results)

with open(fileout, "w") as txt_file:
    txt_file.write(election_results)