import os
import csv

#Import the file to get the data
File = os.path.join("budget_data.csv")

#Create empty lists to house the values of months and revenue
month_names=[]
revenue_values=[]

#Print the beginning statement for analysis
print("Financial Analysis:")
print("----------------------")

#Open file with reader to interpret data
with open(File,"r", newline="") as BankFile:
    csv = csv.reader(BankFile, delimiter=",")

#Put separate columns into lists created above
    next(csv)
    for row in csv:
        # Add title
        month_names.append(row[0])

        # Add revenue
        revenue_values.append(row[1])
    
    #Make values in revenue list into integers
    revenue_values = list(map(int, revenue_values))
    
    #Print total number of months
    print("Total Months: " + str(len(month_names)))
    
    #Calculate and print sum of all values in revenue to find net value    
    Total=sum(revenue_values)
    print("Total: $" + str(Total))

    #Calculate the difference between each month and save to a new list
    differences = [(y-x) for (x, y) in zip(revenue_values[:-1], revenue_values[1:])]
    
    #Calculate the average of all the differences in the list and save to total average, then print value
    total_avg= sum(differences)/len(differences)
    print("Average Change: $" + str(total_avg))

    #Calculate values of greatest increase and greatest decrease
    profit=max(revenue_values)
    deficit=min(revenue_values)

    #Zip month and revenue lists together
    values=zip(month_names,revenue_values)

    #If item at index 1 equals max or min, then print the corresponding values
    for row in values:
        if row[1]>=profit:
            print("Greatest Increase: " + row[0] + " " + "($" + str((row[1])) + ")")

        elif row[1]<=deficit:
            print("Greatest Decrease: " + row[0] + " " + "($" + str((row[1])) + ")")
