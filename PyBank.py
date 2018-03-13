import os 
import csv

totalmonth = 0
totalrevenue = 0
RevenueChange = []
date=[]

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

BankData = os.path.join("Resources","budget_data_1.csv")

with open(BankData, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)

    for row in csvreader:
        date.append(row[0])
        totalmonth = totalmonth + 1
        totalrevenue = totalrevenue + int(row[1])

        if (totalmonth == 1):
            PrRev = int(row[1])
        else:
            Change = (int(row[1]) - int(PrRev))
            RevenueChange.append(Change)
            
        

        PrRev = row[1]
        
    maximum=max(RevenueChange)
    minimum=min(RevenueChange)
    maximum_index=RevenueChange.index(maximum)
    minimum_index=RevenueChange.index(minimum)
    month_max=date[maximum_index +1]
    month_min=date[minimum_index +1]
    print(totalmonth)
    print(totalrevenue)
    print (str(mean(RevenueChange)))
    print (month_max + "(" +str(maximum)+")")
    print (month_min + "(" +str(minimum)+")")



  
    

       










    