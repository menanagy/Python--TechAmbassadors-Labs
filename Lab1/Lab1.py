"""1-Write a program that counts up the number of vowels [a, e, i, o, u]
contained in the string"""

def number_of_vowels(name):
    count = 0
    vowels=["a", "e", "i", "o", "u"]
    for i in name:
        if i in vowels:
            count+=1
    print (f"Number of vowels in {name} is {count}")
#-----------------------------------------------------------------------------------------------
"""
2 - Write a function that accepts two arguments (length, start) to generatean array of 
a specific length filled with integer numbers increased by onefrom start.
"""
def list_fun(start, length):
     my_list = list(range(start, start+length))
     print(my_list)
#-----------------------------------------------------------------------------------------------
"""
3 - Fill an array of 5 elements from the user, Sort it in descending andascending orders then display the output
"""
def sort_array():
    my_list=[]
    num=int(input("Enter the number of elements: "))
    print("Enter the elements: ")

    for i in range(0,num):
        element=int(input())
        my_list.append(element)

    print(my_list)
    my_list.sort()
    print(f"The list in ascending order: {my_list}")
    my_list.sort(reverse=True)
    print(f"The list in descending order: {my_list}")
#-------------------------------------------------------------------------------------------------------
"""
4 -  write a function that takes a number as an argument and if the number divisible by 3 return 
"Fizz" and if it is divisible by 5 return "buzz" and if is isdivisible by both return "FizzBuzz"
"""
def weirdo(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return "whatever"
#-----------------------------------------------------------------------------------------------
"""
5 - Write a function which has an input of a string from user then it will
return the same string reversed
"""
def reverse_string(string):
    #string=input("Enter a string to be reversed: ")
    for i in string:
        new_str = string[::-1]
    print(f"the reversed str: {new_str}")
#-----------------------------------------------------------------------------------------------
"""6 - Ask the user to enter the radius of a circle in order to alert its calculatedarea and circumference"""
def cal_area_circumference():
    r=int(input("Enter a radius to calculate the area: "))
    pi = 3.14
    area = pi * (r**2)
    circumference=2*pi*r
    print(f"area = {area}, circumference={circumference}")

#-----------------------------------------------------------------------------------------------
"""
#7 - Ask the user for his name then confirm that he has entered his name(not an empty string/integers). 
then proceed to ask him for his email andprint all this data- (Bonus) check if it is a valid email or not
"""
import re
def email_is_valid(email):
    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(email_regex, email):
      return True
    else:
      return False
def confirm_name_and_email ():

    name=input("May u enter ur name? ")
    if name and (not name.isdigit()):
        print("Good job, now enter ur email, please")
        email = input()
        if email_is_valid(email):
            print(f"Hello {name}, ur email is: {email}")
        else:
            print("invalid email")

    else:
        print("Wrong input! ")
#-----------------------------------------------------------------------------------------------
"""8 - Write a program that prints the number of times the string 'iti' occurs in"""
def num_of_string_iti_occurs(string):
    numOfOccurence=string.count("iti")
    print("count",numOfOccurence)
#-----------------------------------------------------------------------------------------------
"""
(Bonus) 9 - Write a function that takes a string and prints the longest
alphabetical ordered substring occured.
For example, if the string is 'abdulrahman' then the output is:
Longest substring in alphabetical order is: abdu
"""
def longest_alphabetical(name):

    # initialize
    last = name[0]
    current = last
    longest = last

    # loop letters starting at the second
    for letter in name[1:]:
        if letter >= last:
            current += letter    
        else:
            current = letter  
        if len(current) > len(longest):
            longest = current

        last = letter

    print(longest)
#-----------------------------------------------------------------------------------------------
#Run Functions
#Question1
number_of_vowels("MinaNagy")
#Question2
list_fun(5,10)
#Question3
sort_array()
#Question4
print(weirdo(5))
#Question5
reverse_string("MinaNagyFawzy")
#Question6
cal_area_circumference()
#Question7
confirm_name_and_email()
#Question8
num_of_string_iti_occurs("iti branch nasr city iti smart iti ")
#Question9
longest_alphabetical("abdulrahman")#abdu