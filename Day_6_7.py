
# #######################################################
# ##########################Code -1: List  ##############
# #######################################################
series = []
odd = 0
even = 0

inp = str()

print ("\nEnter the list of numbers. Press 'q' to quit once input is complete\n")
while (inp!='q') :
	inp = input("Enter value:")
	if (inp != 'q'):
	 series.append(inp)
	 

print("\nYou have entered the following series:",series)

for items in series:
	 if (int(items)%2==0):
		 even+=1
	 else:
		 odd+=1

print("\nNumber of even number in the series = {} and number of odd numbers in the series ={}".format(even,odd))

max = int(series[0])
min = int(series[0])
for items in series:
	 if (int(items) > max):
	 	 max = int(items)
	 if (int(items) < min):
	 	 min = int(items)

print ("Maximum value in the series is {} and Minimum value in the series is {}".format(max,min))

count = 0
for x in range((len(series))//2):
	 if(series[x]!=series[len(series)-1-x]):
		 count+=1

if(count==0):
	print("The series is a palindrome")
else:
	print("The series is not a palindrome")


for x in range(len(series)):
	 temp1 = list(series[x])
	 temp2 = temp1[::-1]
	 if (temp1 == temp2):
	 	 print("{} is palindrome.".format(series[x]))
	 


	 