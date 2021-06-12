#####################################
#######Code -1: Age Calculator#######
#####################################

from datetime import date
print ("\nThis code will calculate your current age")

name = input("Enter your name: ")
dd = int(input ("Enter Date between 1 to 31: "))
mm = int(input ("Enter Month - Jan =1, Feb =2, ...Dec = 12: "))
yyyy = int(input ("Enter Year in YYYY: "))

date_today = date.today()
date_birth = date(yyyy, mm, dd)
days_difference = (date_today - date_birth).days
age_years = int(days_difference//365.2425)
age_month = (days_difference - age_years*365)*12//365

print("\nYour date of date of Birth is ",date_birth)
print("Hi {}. Your age as of today is {} years, {} months.".format(name, age_years, age_month))
print("\n**end of code**\n")


############################################
#######Code -2: Arithmatic Calculator#######
############################################

print ("\nThis code is a calculator")

print('''Please enter the calculation you want to perform
         1 - Addition
         2 - Subtract
         3 - Multiplication
         4 - floor division
         5 - Decimal division
         6 - Remainder
         7 - Exponential'''
    ) 
option = int(input ())
a = float(input("Enter the first number: "))
b = float(input("Enter the second  number: "))

print ("the option selected is:", option)
if option == 1:
	c = a+b
elif option == 2:
	c = a-b
elif option == 3:
	c = a*b
elif option == 4:
	c= a//b
elif option == 5:
	c=a/b
elif option == 6:
	c=a%b
elif option == 7:
	c=a**b

print("\nThe output=", c)
print("\n**end of code**\n")