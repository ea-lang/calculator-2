# """
# calculator.py

# Using our arithmetic.py file from Exercise02, create the
# calculator program yourself in this file.
# """

from arithmetic import *


# # Your code goes here

def my_reduce(function,calc_list):
    for i in range(len(calc_list)):
        if i == (len(calc_list))-1:
            return calc_list
        else:
            calc_list[i:i+2] = function(calc_list[i], calc_list[i+1]) 

 
while True:
    input_string = raw_input("> ")
    input_list = input_string.split(" ")
    if input_string.lower() == "q" or input_string.lower() == "quit":
        break
    
    elif input_list[0] == "+":
        print reduce(add, map(int, input_list[1:]))
    
    elif input_list[0] == "-":
        print reduce(subtract, map(int, input_list[1:]))
    
    elif input_list[0] == "*":
        print reduce(multiply, map(int, input_list[1:]))
    
    elif input_list[0] == "**":
        print power(int(input_list[1]), int(input_list[2]))
    
    elif input_list[0] == "%":
        print mod(int(input_list[1]), int(input_list[2]))
    
    elif input_list[0] == "/":
        print reduce(divide, map(int, input_list[1:]))
    
    elif input_list[0] == "square":
        print square(int(input_list[1]))
    
    elif input_list[0] == "cube":
        print cube(int(input_list[1]))
    
    else:
        print "Not a valid input. Please try again"
