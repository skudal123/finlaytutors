


def hello(name):
    name = name.lower() 
    name = name.capitalize()
    print("Hi " + name + "!")

nameslist = []
with open("C:\\Users\\Finlay.Edwards\\Documents\GitHub\\finlaytutors\\working with files or something\\names.txt") as file:
    for line in file:
        line = line.strip()
        nameslist.append(line)


for name in nameslist:
    hello(name)

