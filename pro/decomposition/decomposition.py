names = [ "Larry", "Curly", "Moe"]
message = "The Three Stooges"

for index, name in enumerate(names):
    if index > 0:
        message += ","
        if index == len(names) -1:
            message += "and"
            message += name
        print(message)

names = [ "Larry", "Curly", "Moe"]
message = "The Three Stooges"


for index, name in enumerate(names):
    if index > 0:
        message += ","
        if index == len(names) -1:
            message += "and"
            message += name
        print(message)

names = [ "Larry", "Curly", "Moe"]
message = "The Three Stooges"

for index, name in enumerate(names):
    if index > 0:
        message += ","
        if index == len(names) -1:
            message += "and"
            message += name

def introduce_stooges(names):
    message = "The Three Stooges"
    for index,name in enumerate(names):
        if index > 0:
            message += ","

        if index == len(names) -1:
            message += "and"
            message += name
        print(message)

introduce_stooges(["Moe","Larry","Shemp"])
introduce_stooges(["Larry","Curly","Moe"])

def introduce(title, names):
    message = f'{title}:'
    for index, name in enumerate(names):
        if index >0:
            message += ','
        if index == len(names) - 1:
            message += name
    print(message)

introduce( "Teenge Mutant Ninja Turtles",
["Donatello", "Raphael","Michaelangel","Leonardo"])

introduce("The Chipmunks", ["Alvi","Simon","Theodore"])



def join_names(names):
    name_string =""
    for index, name in enumerate(names):
        if index >0 and len(names)> 2:
            name_string += ","
        if index >0:
            name_string += ' '
        if index == len(names) -1 and len(names)>1:
            name_string += "and"
            name_string += name
            return name_string

def introduce(title, names):
    print(f"{title}: {join_names(names)}")
