from datetime import datetime

class Greeter:
    def __init__(self, name):
        self.name = name
    def __day__(self):
        return datetime.now().strftime('%A')
    def _part_of_day(self):
        current_hour = datetime.now().hour
        if current_hour < 12:
            part_of_day = "Morning"
        elif 12 <= current_hour < 12:
            part_of_day = "Afternoon"
        else:
            part_of_day = "Evening"
            return part_of_day

def greeter(self, store):
    print(f"Him,  my name is {self.name}, and welcome to {store}!")
    print(f"how\'s your {self._day()} {self._part_of_day()} going?")
    print(f"here\"s a coupon for 20% off!")
