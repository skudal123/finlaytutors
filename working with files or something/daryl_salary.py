import csv

def doNothing():
    return

def getinfo(name, department, birthday, salary):
    print(name + " works in " + department + ", they have a birthday in " + birthday + " and has a salary of £" + salary)
  
NameList = []
DeptList = []
BonusList = []


with open("E:\\Git Repos\\Fin Py Mastermind\\finlaytutors\\working with files or something\\employeebirthday.csv") as csv_file:
    dictionary=csv.DictReader(csv_file)
    for row in dictionary:
        NameList.append(row["Name"])
        DeptList.append(row["Department"])
        if row['Salary'] > "50000":
            BonusList.append(round(int(row["Salary"])*0.05,2))
        elif row['Salary'] <= "50000":
            BonusList.append(round(int(row["Salary"])*0.07,2))
        
with open("E:\\Git Repos\\Fin Py Mastermind\\finlaytutors\\working with files or something\\bonus.csv", 'w', newline='') as csv_file:
    Fields=['Name','Department','Bonus']
    csvwriter=csv.DictWriter(csv_file, fieldnames=Fields)
    csvwriter.writeheader()
    for i in range(len(NameList)):
        csvwriter.writerow({'Name': NameList[i], 'Department':DeptList[i], 'Bonus':BonusList[i]})


