class GuessNumber:
    def __init__(self, number, mn=0, mx=100):
        self.number = number
        self.guesses = 0
        self.min = mn
        self.max  = mx
        
    def get_guess(self):
        guess = input(f"Please guess a number ({self.min} - {self.max}):")

        if self.valid_number(guess):
            return int(guess)
        else:
            print("Please enter a valid number.")
            return self.get_guess()

    def valid_number(self, str_number):
        try:
            number = int(str_number):
        except:
            return False

