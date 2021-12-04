"""
Name: Romario Linares
File: model_candybar.py
Description: Modeling a candy bar using a custom base class and encapsulation for its data variables. The main function will take in a series
of inputs, where the methods of the base class will display properties for three candy bars: KitKat, Snickers, and Twix. The function
will output the candy coating, filling, size, and wafer type of the candy bar and also write out each of the outputs in a text file
called 'candybarprofile.txt'.

BEFORE RUNNING CODE MAKE SURE YOU TYPE IN CMD TERMINAL 'pip install pyfiglet'.

"""
# pip install pyfiglet
import pyfiglet as fig
import random

# Implement base class 'CandyBar'
class CandyBar:
   # __init__ method takes the candy bar identifier, coating and filling ingredient, and integer for size of candy bar from main function
    def __init__(self, candybar, coating, filling, size):
        # __init__ method stores 'self.__candybar' as main identifier for different types of candy bars
        self.__candybar = candybar
        # Calling the set functtions, and assigning input_coat/input_fill from it as the coating/filling data attribute
        self.set_coating(coating)
        self.set_filling(filling)
        self.__size = size
        # Casting data variables as empty strings
        self.__wafer = ""
        self.__expiration_type = ""
        # Casting self.__expiration to a list of three integers that is randomly generated in between the range of 1-20
        self.__expiration = [random.randrange(1, 20, 1) for i in range(3)]

    # Get method returns the private data variable for the coating type
    def get_coating(self):
        return self.__coating
    # Get method returns the private data variable for the filling type
    def get_filling(self):
        return self.__filling
    
    # Set method assigns 'input_coat' data variable to 'self.__coating', and uses if then statement to detect if main function
    # has either "chocolate", "strawberry", or "white chocolate" as 'coating' for CandyBar
    def set_coating(self, input_coat):
        if ((input_coat == "chocolate") or (input_coat == "strawberry") or (input_coat == "white chocolate")):
            # Makes the string fully uppercase, and returns whatever coating type was detected from main function in 'get_coating(self)' method
            self.__coating = input_coat.upper()
    # Set method assigns 'input_fill' data variable to 'self.__filling', and uses if then statement to detect if main function
    # has either "chocolate", "caramel", or "peanuts" as 'filling' for CandyBar
    def set_filling(self, input_fill):
        if ((input_fill == "chocolate") or (input_fill == "caramel") or (input_fill == "peanuts")):
            # Makes the string fully uppercase, and returns whatever filling type was detected from main function in 'get_filling(self)' method
            self.__filling = input_fill.upper()
        
    def is_size(self):
        # Uses if in range loop in order to assign 'self.__size' data variable as either "Mini", "Regular", or "Party Size!" for each candy bar
        if self.__size in range(1, 10):
            # Uppercases the output so that when displayed in the final string representation it looks like "MINI", "REGULAR", or "PARTY SIZE"
            format_size = ("Mini").upper()
            return(format_size)
        elif self.__size in range(10, 21):
            format_size = ("Regular").upper()
            return(format_size)
        # If the size is over any of the previous numerical ranges, then self.__size is automatically assigned as the largest candy size
        elif self.__size >= 21:
            format_size = ("Party Size!").upper()
            return(format_size)

    def is_wafer(self):
        if type(self.__expiration) != str:
            # Assigns variable 'average' to the average of the each randomized list of integers in self.__expiration
            average = sum(self.__expiration) / len(self.__expiration)
            # 50% chance of being brittle
            if average < 10:
                self.__wafer = "Brittle Wafer"
                # Assigns what type of expiration candy bar is in empty string of self.__expiration_type
                self.__expiration_type = "Already Expired".upper()
            # 25% chance of being crusty
            elif average < 15:
                self.__wafer = "Crusty Wafer"
                # Assigns what type of expiration candy bar is in empty string of self.__expiration_type
                self.__expiration_type = "Not Expired".upper()
            # 25% chance of being strong
            else:
                self.__wafer = "Strong Wafer"
                # Assigns what type of expiration candy bar is in empty string of self.__expiration_type
                self.__expiration_type = "Too Fresh".upper()
        # Formats self.__wafer into the pip install pyfiglet font format to make ASCII font art
        format_wafer = (fig.figlet_format(self.__wafer))
        return(format_wafer)

    # __str__ method returns the string representation as table of each data variable from each method that was inputted from main function
    def __str__(self):
        # Looks like "{CandyBarType} = Size: {CandySize}, Coating: {IngredientCoating}, Filling: {FillingIngredient}, Expiration Date: {ExpirationType}" repeated x3
        return(f"{self.__candybar} = Size: {self.is_size()}, Coating: {self.get_coating()}, Filling: {self.get_filling()}, Expiration Date: {self.__expiration_type} \n {self.is_wafer()}")
        

# Main function (Demo Program)
def main():
    # open text file as f
    with open("candybarprofile.txt", "r+") as f:
        # f.truncate(0) clears any contents that are in candybarprofile.txt
        f.truncate(0)
        # Writes this string on the very top of the file before any of the candy bar profiles appear later on from main function
        f.write("Candybar Profiles:")
        f.close()
    # variable is set to 0 to begin 3x loop
    x = 0
    while True:
        # The candy bar type, coating ingredient, and filling ingredient are randomly chosen from their string list within each turn of 
        # the while True loop using the random.choice method.
        candybars = random.choice(['KitKat', 'Snickers', 'Twix'])
        coatings = random.choice(['chocolate', 'strawberry', 'white chocolate'])
        fillings = random.choice(['chocolate', 'caramel', 'peanuts'])

        # Setting three randomized candy bar types with their type, coating ingredient, filling ingredient, and randomized size integer
        candy_profiles = CandyBar(candybars, coatings, fillings, random.randrange(1,30))
        print(candy_profiles)
        # open text file as f
        with open("candybarprofile.txt", "a") as f:
            f.write(f"\n{str(candy_profiles)}")
        # After program finishes, x = 0 is added by 1 each loop turn
        x += 1
        # When x reaches the value of 3, then we close file while True loop will stop
        if x == 3:
            f.close()
            break

# Call main function
if __name__ == "__main__":
    main()