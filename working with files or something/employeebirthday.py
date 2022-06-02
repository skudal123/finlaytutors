import csv

def doNothing():
    return

def getinfo(name, department, birthday):
    print (name + " works in " + department + " and has a birthday in " + birthday + ".")

#getinfo("John", "Jumping", "June")

    
Gardeners = []

with open("C:\\Users\\Finlay.Edwards\\Documents\GitHub\\finlaytutors\\working with files or something\\employeebirthday.csv") as csv_file:
    dictionary=csv.DictReader(csv_file)   
    for row in dictionary:
        if row['Department'] != "Gardening":
            doNothing
        else:
            getinfo(row['Name'], row['Department'], row['BirthdayMonth'])
            Gardeners.append(row['Name'])
        
with open("C:\\Users\\Finlay.Edwards\\Documents\GitHub\\finlaytutors\\working with files or something\\gardeners.csv", 'w', newline='') as csv_file:
    Field=['Name']
    csvwriter=csv.DictWriter(csv_file, fieldnames=Field)
    csvwriter.writeheader()
    for name in Gardeners:
        csvwriter.writerow({'Name': name})

        #new csv file that has name,department,bonus but anyone paid over 50000 get only 5% (7% normaly)

        #salary/100*7


