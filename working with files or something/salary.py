import csv

namelist=[]
departmentlist=[]
birthdaylist=[]
salarylist=[]

def getinfo(name, department, birthday, salary):
    print(name + " works in " + department + ", they have a birthday in " + birthday + " and has a salary of £" + salary)

with open("C:\\Users\\Finlay.Edwards\\Documents\GitHub\\finlaytutors\\working with files or something\\employeebirthday.csv") as csv_file:
    dictionary=csv.DictReader(csv_file)
    for row in dictionary:
        if row['Salary'] >= "50000":
            getinfo (row["Name"], row["Department"], row["BirthdayMonth"], row['Salary']/100*7)
            namelist.append(row["Name"])
            departmentlist.append(row["Department"])
            birthdaylist.append(row["BirthdayMonth"])
            salarylist.append(row["BirthdayMonth"])
        elif row['Salary'] < "50000":
            getinfo (row["Name"], row["Department"], row["BirthdayMonth"], row['Salary']+row["Salary"]/100*5)
            namelist.append(row["Name"])
            departmentlist.append(row["Department"])
            birthdaylist.append(row["BirthdayMonth"])
            salarylist.append(row["BirthdayMonth"])

with open("C:\\Users\\Finlay.Edwards\\Documents\GitHub\\finlaytutors\\working with files or something\\salary.csv", 'w', newline='') as csv_file:
    Field=['Name']
    csvwriter=csv.DictWriter(csv_file, fieldnames=Field)
    csvwriter.writeheader()
    for name in namelist:
        csvwriter.writerow({'Name': name})

with open("C:\\Users\\Finlay.Edwards\\Documents\GitHub\\finlaytutors\\working with files or something\\salary.csv", 'w', newline='') as csv_file:
    Field=['Department']
    csvwriter=csv.DictWriter(csv_file, fieldnames=Field)
    csvwriter.writeheader()
    for department in departmentlist:
        csvwriter.writerow({'Department': departmentlist})

with open("C:\\Users\\Finlay.Edwards\\Documents\GitHub\\finlaytutors\\working with files or something\\salary.csv", 'w', newline='') as csv_file:
    Field=['BirthdayMonth']
    csvwriter=csv.DictWriter(csv_file, fieldnames=Field)
    csvwriter.writeheader()
    for birthday in birthdaylist:
        csvwriter.writerow({'BirthdayMonth': birthdaylist})

with open("C:\\Users\\Finlay.Edwards\\Documents\GitHub\\finlaytutors\\working with files or something\\salary.csv", 'w', newline='') as csv_file:
    Field=['Salary']
    csvwriter=csv.DictWriter(csv_file, fieldnames=Field)
    csvwriter.writeheader()
    for salary in salarylist:
        csvwriter.writerow({'Salary': salarylist})


