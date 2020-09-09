import os
import csv

csvpath = os.path.join('budget_data.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}") 
   

    months = []
    profit = []
    change = []

    
   
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change.append(profit[i+1]-profit[i])
                      

increase = max(change)
decrease = min(change)


month_increase = change.index(max(change))+1
month_decrease = change.index(min(change))+1


print ("Financial Analysis")
print ("------------------------")
print (f"Total Months:{len(months)}")
print (f"Total: ${sum(profit)}")
print (f"Average Change: {round(sum(change)/len(change),2)}")
print (f"Greatest Increase in Profits: {months[month_increase]} (${(str(increase))})")
print (f"Greatest Decrease in Profits: {months[month_decrease]} (${(str(decrease))})")
   
csvpath_output = os.path.join("outfile.txt")
with open(csvpath_output, "w") as txt_file:
    txt_file.write ("Financial Analysis")
    txt_file.write ("------------------------")
    txt_file.write (f"Total Months:{len(months)}")
    txt_file.write (f"Total: ${sum(profit)}")
    txt_file.write (f"Average Change: {round(sum(change)/len(change),2)}")
    txt_file.write (f"Greatest Increase in Profits: {months[month_increase]} (${(str(increase))})")
    txt_file.write (f"Greatest Decrease in Profits: {months[month_decrease]} (${(str(decrease))})")