------------------------------
Name: Romario Linares
Script Name: model_candybar.py
Date: 12/2/2021
GitHub Link: https://github.com/romariolinares1/Modeling-Candy-Bars 
------------------------------
Description of Class: 
NOTE: BEFORE RUNNING 'model_candybar.py', MAKE SURE YOU INPUT 'pip install pyfiglet' IN THE CMD TERMINAL

The script only takes in a single base class. This class being called 'CandyBar'. The class contains a total
of eight methods. One __init__ method, one __str__ method, two get methods, two set methods, and two other non get-set methods. From the 
main function, the class will take in a candy bar type, candy coating ingredient, candy filling ingredient, the size of the candy, and
the expiration type of the candy bar itself. The main function will then print out each individual candy bar type as variables,
which will then be represented as a table of three different candy bars with their different coatings, fillings, sizes, and expirations. 
The outputs from the main function are also written in an external text file called 'candybarprofile.txt'. There, also writes down 
the wafer type of the candy bar for whether the wafer is BRITTLE, CRUSTY, or HARD in ASCII font.
------------------------------
Description of Data Variables:
NOTE: Each data variable is encapsulated, therefore, they are written as private variables for most of them.

* self.__candybar: This data variable is the identifier of the candybar. It is the very first string variable that is inputted in the 
                   main function, and identifies which candybar the class will identify as.
* self.__coating: This data variable takes in an ingredient from a random list of string ingredients like 'chocolate', 'strawberry', and
                  'white chocolate'. It acts as the first layer when modeling a candy bar, as it represents the candy coating of it.
* self.__filling: Similar to self.__coating, this data variables also takes in an ingredient from a random list of strings like 'chocolate',
                  'caramel', and 'peanuts'. It represents the candy filling of the candy bar, and is the second layer when modeling the
                  candy bar itself.
* self.__size: Even if defined in the __init__ method of the base class, self.__size is actually set in the main function (demo program) as
               a randomly generated integer from a range of numbers. This data variable takes that randomly generated integer, and returns
               a string that indicates the size of the candy bar based on if the integer for self.__size is within a certain range of numbers.
* input_coat: This data variable acts as the placeholder for whatever string was inputted in the main function in the list of each candy bar.
              It is used to set the input uppercased when listing out each of the layers/ingredients of the finalized candy bars.
* input_fill: Similar to input_coat, input_fill works the exact same way. Using a get-set method like used for input_coat, the exact
              process is conducted but for 'chocolate', 'caramel', and 'peanuts' instead of 'chocolate', 'strawberry', and 'white chocolate'.
* self.__wafer: This data variable is assigned an empty string at first, but returns the wafer type when running the file. The wafer type
                is determined based the average of the expiration date list, and has three types: 'BRITTLE WAFER', 'CRUSTY WAFER', & 'STRONG WAFER'
* self.__expiration_type: This data variable is also assigned an empty string at first, but returns the type of expiration in the text
                          file. It is also determined from the expiration date list, and also has three types: 'ALREADY EXPIRED', 
                          'NOT EXPIRED', & 'TOO FRESH'.
* self.__expiration: In self.__expiration, we assign this data variable to a list of three random integers between 1-20 in the __init__ 
                     method. The function then returns the average of the list to set a numerical value as the expiration that sets 
                     self.__expiration_type and self.__wafer.
------------------------------
Description of Methods:
* def __init__(): The __init__() method stores all of the private data variables for the CandyBar base class. It also stores the identifier
                  for the candy bar itself, the empty strings for self.__wafer and self.__expiration_type.
* def get_coating(): This method is the first get method of the get-set pair. It returns the data variable for self.__coating, which is
                     attained in def set_coating().
* def get_filling(): This method is the second get method of the get-set pair. It returns the data variable for self.__filling, which is
                     attained in def set_filling().
* def set_coating(): In this method, the funciton uses the data variable input_coat in order to assign set_coating() as an uppercased string
                     for the string coating ingredient selected randomly from the list in the main function.
* def set_filling(): In this method, the funciton uses the data variable input_fill in order to assign set_filling() as an uppercased string
                     for the string filling ingredient selected randomly from the list in the main function.
* def is_size(): The is_size() method detects whether the randomly generated size fits into specific ranges. If the size fits into the
                 specific ranges listed, it will either return 'MINI', 'REGULAR', or 'PARTY SIZE!' based on how high the number of 
                 self.__size is.
* def is_wafer(): For this method, the function takes the average of self.__expiration, by taking the sum of the lists generated and the
                  length of the lists generated. Based on how large the average is in numerical value, the program will return three types
                  of wafers. These types are 'BRITTLE WAFER', 'CRUSTY WAFER', & 'STRONG WAFER', which will be returned as ASCII art in the
                  text file.
* def __str__(): The __str__() is simply a method that just takes specific methods, and specific data variables from each of the methods of
                 the class. As it stores all the data acquired from the methods, __str__() returns a string representation that showcases
                 each of the candy bar types with their correlated ingredients, sizes, and expiration types.
------------------------------
Description of Demo Program (main()):
In this script, we write a demo program within our main function. The demo program starts off with clearing any data that was written into
the output text file 'candybarprofile.txt'. This is to make sure the program starts fresh for each different candy bar profile generated.
After this, the demo program will go through a while True loop about 3 times. Inside the while True loop, the funciton sets three candy bar
profiles using the CandyBar base class to implement its ingredients and different layers to model each profile. Each of these ingredients
and inputs are detected as private data variables within the __init__() method in CandyBar(). The demo program then creates three sets of
lists, where the function will choose a random string value from that list, and assign it as each private data variable in the __init__()
method of Candybar(). After all of this, once each output is returned through each of the methods in the main base class, the demo program
will write its contents in the form of tabled/individual profiles with ASCII art in the output file 'candybarprofile.txt'.

Instructions:
Before running the main python code 'model_candybar.py', make sure you type into the terminal 'pip install pyfiglet'. This will allow
the program to use the ASCII art formatting that is in the pyfiglet package when imported. Make sure you  also have 'candybarprofile.txt' 
open as well before running the code so you will be able to see the changes in the output file when running the code.
------------------------------
Example of Final Output in the Text File:

Candybar Profiles:
KitKat = Size: PARTY SIZE!, Coating: CHOCOLATE, Filling: CARAMEL, Expiration Date: NOT EXPIRED
   ____                _          __        __     __           
 / ___|_ __ _   _ ___| |_ _   _  \ \      / /_ _ / _| ___ _ __ 
| |   | '__| | | / __| __| | | |  \ \ /\ / / _` | |_ / _ \ '__|
| |___| |  | |_| \__ \ |_| |_| |   \ V  V / (_| |  _|  __/ |   
 \____|_|   \__,_|___/\__|\__, |    \_/\_/ \__,_|_|  \___|_|   
                          |___/                                

Twix = Size: REGULAR, Coating: STRAWBERRY, Filling: CHOCOLATE, Expiration Date: ALREADY EXPIRED
  ____       _ _   _   _       __        __     __           
| __ ) _ __(_) |_| |_| | ___  \ \      / /_ _ / _| ___ _ __ 
|  _ \| '__| | __| __| |/ _ \  \ \ /\ / / _` | |_ / _ \ '__|
| |_) | |  | | |_| |_| |  __/   \ V  V / (_| |  _|  __/ |   
|____/|_|  |_|\__|\__|_|\___|    \_/\_/ \__,_|_|  \___|_|   
                                                            

Snickers = Size: REGULAR, Coating: WHITE CHOCOLATE, Filling: PEANUTS, Expiration Date: TOO FRESH 
  ____  _                          __        __     __           
/ ___|| |_ _ __ ___  _ __   __ _  \ \      / /_ _ / _| ___ _ __ 
\___ \| __| '__/ _ \| '_ \ / _` |  \ \ /\ / / _` | |_ / _ \ '__|
 ___) | |_| | | (_) | | | | (_| |   \ V  V / (_| |  _|  __/ |   
|____/ \__|_|  \___/|_| |_|\__, |    \_/\_/ \__,_|_|  \___|_|   
                           |___/                       
