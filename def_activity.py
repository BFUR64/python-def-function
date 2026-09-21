# A def function is used to define a reusable block of code that can
# be called whenever that functionality is needed.
#
# SUMMARY:
# This program demonstrates a chain of 10 function calls.
# Functions 1-5 double the input string.
# Functions 6-10 calculate and pass along counts based on the
# string and all previously generated counts.
# The final function displays the resulting string and counts.
#
# WHAT IS A FUNCTION?
# A `def` function is used to define a reusable block of code that can
# be called whenever that functionality is needed.

user_string = input("Enter a string: ")

# Function 1: Doubles the input string and passes it to function 2.
def print1():
    string = user_string * 2
    print2(string)


# Function 2: Doubles the string again and passes it to function 3.
def print2(string):
    string = string * 2
    print3(string)


# Function 3: Doubles the string again and passes it to function 4.
def print3(string):
    string = string * 2
    print4(string)


# Function 4: Doubles the string again and passes it to function 5.
def print4(string):
    string = string * 2
    print5(string)


# Function 5: Performs the final string doubling and starts the counting phase.
def print5(string):
    string = string * 2
    print6(string)


# Function 6: Counts the characters in the string.
def print6(string):
    count1 = len(string)
    print7(string, count1)


# Function 7: Counts the string plus the first count.
def print7(string, count1):
    count2 = len(string + str(count1))
    print8(string, count1, count2)


# Function 8: Counts the string plus all previous counts.
def print8(string, *counts):
    new_count = len(string + "".join(map(str, counts)))
    print9(string, *counts, new_count)


# Function 9: Adds another count and passes everything to the final function.
def print9(string, *counts):
    new_count = len(string + "".join(map(str, counts)))
    print10(string, *counts, new_count)


# Function 10: Calculates the final count and displays the results.
def print10(string, *counts):
    final_count = len(string + "".join(map(str, counts)))

    print("String:", string)
    print("Counts:", *counts, final_count)


# Invoke the first function to start the chain.
print1()
