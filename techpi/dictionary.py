# how to used a dict
customer_1 =  {"username": "Jhon-sea", "online": False, "Friends":100}
print(customer_1.keys())


newlist = {}
otherlist = dict()

new_list = {
    "Brand":"Honda", "Model":"Civic", "Year": 1995
}
x =  new_list["Brand"]
print(x)

# new_list.keys() ,new_list.values(), new_list.items()

new_list["Year"] = 2018
print(new_list)
# loop through dict print all dictionary
for x in new_list:
    print(x)

for x in new_list:
    print(new_list[x])

for x, y in new_list.items():
    print(x,y)



