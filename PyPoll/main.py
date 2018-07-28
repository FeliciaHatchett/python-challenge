import os
import csv

file = os.path.join("election_data.csv")

with open(file,"r", newline="") as filename:
    csv=csv.reader(filename, delimiter=",")