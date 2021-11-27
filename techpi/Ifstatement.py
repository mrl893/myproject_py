if 5 > 1:
    print("That's True")

x = 35
if x > 20:
    print("Above twenty")
    if x > 30:
        print("and also above 30!")

# elif
a = 45
b = 45
if b > a:
    print("b is greater than a")
elif   a == b:
    print("a and b are aqual")


age = 4
if age < 4:
    ticket_price = 0
elif  age < 18:
    ticket_price = 10
else:
    ticket_price = 15

new_list = [1,2,3,4]
x = 10
if x not in new_list:
    print("x isn't on the list, so this is True")


# Pass statements
a = 33
b = 200

if b > a:
    pass

# for loop

for x in "apple":
    print(x)

# while loop
i = 1
while i < 8:
    print(x)
    i += 1
i = 1
"""""while i < 8:
    print(x)
    if i == 4:
        if i == 4:
            break
            i += 1
"""""


# class and subclass
class  car(object):
    """doctype"""
    def __init__(self, color, doors, tires):
        self.color = color
        self.doors = doors
        self.tires = tires
    def brake(self):
        """
        stop the car
        """
        return "Braking"
    def driver(self):
        """
        driver the car
        """
        return "i'm driving"

class Car(object):
    """
    The car class
    """
    def brake(self):
        """
        Overwrite brake method
        """
        return "the car is braking slowly!"
if __name__ == '__main__':
    car.Car("")
    car.brake()
    "The car is class is breaking slowly!"
    car.drive()
    "I'm driving a yellow car!"

