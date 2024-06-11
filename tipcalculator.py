# print("Hello "+input("What is your name?")+"! Nice to meet you!") #This is a simple program that greets the user by their name.

# a=input()
# b=input()
# c=a
# a=b
# b=c
# print("a:"+a)
# print("b:"+b)
# #This program swaps the values of two variables without using a temporary variable.


# print("hello"[0]) way to pull out the element of the element from any string 
# print("hello"[0:3]) way to pull out the element of the element from any
# print("Hello"[-1])
# mystery =734_529.678

# "524" is a string as anyrthiong inside " " is a string 

# print(type(num_char)) gives what type of data tyope num_char is basically to check what datatype it is 

# a=123
# print(type(a)) gives output <class 'int'>

# two_digit_number = input()
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])

# #Add the two intetegers together by taking input 
# two_digit_number= first_digit + second_digit
# print(two_digit_number)    

# print(3+5)
# print(7-1)
# print(3*2)
# print(6/3)
# print(2**3) #exponentiation
# print(5//2) #integer division
# print(5%2) #modulus
# print(5/2) #float division
#for mathematical operations 
#PEMDAS p-parenthesis
#E-exponentiation
#M-multiplication
#D-division
#A-addition
#S-subtraction
# print(3*(3+3)/3-3) #example of pemdas rule answer is 3.0

#bmi calculator 
# height=input()
# weight=input()
# weight_as_int = int(weight)
# height_as_float =float(height)
# bmi=weight_as_int/(height_as_float*height_as_float)
# bmi_as_int =int(bmi) to get bmi as whole number 
# print(bmi_as_int)
# print(round(8/3,2)) it rounds the number till 2 decimal places answer is 2.67
# print(8//3) it gives the quotient answer is 2     it diresctly gives round number it is called as floor division 

# score =0
# score = score +1 or score += 1 both are same  
# print(score) answer is 1
# += -= *= /= %= //= **= are all augmented assignment operators

# score=0
# height=1.8
# isWinning=True
# #fstring
# print(f"your score is {score}, your height is {height} and you are winning is {isWinning}") by using fstring you can use any data type with string
#remember always use {} brackets for using taking other data values in fstring 

#tip calculator 
print("Welcome to the tip calculator!")
bill=input("What was the total bill? $")   #always remember whenever we take input and write input in number it is string format so we need to coonvert it in integer of float 
bill_as_float=float(bill)
tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
people= int(input("How may people to split the bill?"))
bill_with_tip = tip / 100 * bill_as_float + bill_as_float
print(bill_with_tip)
bill_per_person= bill_with_tip / people
final_amount=round(bill_per_person, 2)
print(f"Each person should pay ${final_amount:.2f}")