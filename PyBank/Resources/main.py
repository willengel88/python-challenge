import os
import csv

#Reading in CSV file
#Csv file is in the same folder as python file
csv_data= os.path.join("budget_data_1.csv")

with open(csv_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the first row of the csv
    next(csv_reader, None)

    Date= []
    Revenue=[]
    increase_revenue=[]
    maxim=0
    
    # Loop through rows
    for row in csv_reader:
          #print(row)
          #putting row of dates into empty list called Date
          Date.append(row[0])
          # putting row of revenue in epty list called Revenue
          Revenue.append(int(row[1]))

    print("Financial Analysis")
    print("------------------------------------")
    print("Total Months: " + str(len(Date)))
    print("Total Revenue: " +"$"+ str(sum(Revenue)))
    
    # looping from the list of Revenue to subtract each revenue with the one before it.
    # the loop starts from index 1 rather than 0 because I do not want to subtract the first revenue from anything
    for i in range(1, len(Revenue)):
        change_rev= Revenue[i]-Revenue[i-1]
        increase_revenue.append(change_rev)
        
    
    # using max and min function to find the index of max and min change in the diff in revenue  
    max_index= increase_revenue.index(max(increase_revenue))
    min_index= increase_revenue.index(min(increase_revenue))
    print("Average Revenue Change: " +"$" + str(sum(increase_revenue)/len(increase_revenue)))
    print("Greatest Increase in Revenue: " + Date[max_index+1] + " ($" + str(increase_revenue[max_index])+ ")")
    print("Greatest Decrease in Revenue: "  + Date[min_index+1] + " ($" + str(increase_revenue[min_index])+ ")")

  
