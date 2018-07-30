import os
import csv

#Import the file to get the data
File = os.path.join("budget_data.csv")
Fileout="Financial_Analysis.txt"
#Create empty lists to house the values of months and revenue
month_names=[]
revenue_values=[]


#Open file with reader to interpret data
with open(File,"r", newline="") as BankFile:
    csv = csv.reader(BankFile, delimiter=",")

#Put separate columns into lists created above
    next(csv)
    for row in csv:
        # Add title
        month_names.append(row[0])

        # Add revenue
        revenue_values.append(int(row[1]))
   
    #Calculate and print sum of all values in revenue to find net value 
    Total=sum(revenue_values)
    
    #Calculate the difference between each month and save to a new list
    differences = [(y-x) for (x, y) in zip(revenue_values[:-1], revenue_values[1:])]
    
    #Calculate the average of all the differences in the list and save to total average
    total_avg= sum(differences)/len(differences)
    
    #Zip differences with month names associated with the y values
    profit_losses=list(map(list, zip(month_names[1:], differences[:])))    

    
    #Calculate values of greatest increase and greatest decrease
    profit=max(differences)
    deficit=min(differences)

    #If item at index 1 equals max or min, then print the corresponding values
    for row in profit_losses:
        if row[1]>=profit:
            winner=row[0]
            profit=row[1]
            

        elif row[1]<=deficit:
            loser=row[0]
            deficit=row[1]

#Save final statement to single variable for export
financial_analysis=(f"Financial Analysis:\n"
                        f"----------------------\n"
                        f"Total Months: {(len(month_names))}\n"
                        f"Total: ${Total}\n"
                        f"Average Change: ${total_avg}\n"    
                        f"Greatest Increase: {winner} (${profit})\n"
                        f"Greatest Decrease: {loser} (${deficit}))\n")
print(financial_analysis)

with open(Fileout, "w") as txt_file:
    txt_file.write(financial_analysis)