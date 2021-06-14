#####################################################
#######Code -1: occurenece of 'y' in a string #######
#####################################################
print("\n***********************Start of code*******************************")
print("This programme calculates the number of occureneceof 'y'in the string")
st_1 = input("Enter the string:")
print("\nThe letter 'y' occurs {} time(s) in the string you have entered".format(st_1.count('y')+st_1.count('Y')))
print("**************************End of Code********************************")


#####################################################
#######Code -2: Even Indexed characters #######
#####################################################
print("\n***********************Start of code*******************************")
print("This programme prints even indexed characters in the string")
st_1 = input("Enter the string:")
print("\nEven indexed letters are {}".format(st_1[::2]))
print("**************************End of Code********************************")


#####################################################
#######Code -3: Swap case #######
#####################################################
print("\n***********************Start of code*******************************")
print("This programme swaps the cases in the string")
st_1 = input("Enter the string:")
print("\nString after swapcase is: {}".format(st_1.swapcase()))
print("**************************End of Code********************************")