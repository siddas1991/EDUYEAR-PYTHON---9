#######################################################
# #Code -1: All numbers between n to m divisible by 5 &7#
# #######################################################
print()
lower_b,higher_b = int(input("Enter the lower bound number:")), int(input("Enter the higher bound number:"))
list_5 =[]
list_7 =[]
list_35 =[]

print("\nYou have entered lower bound as {} and higher bound as {}".format(lower_b,higher_b))
for x in range(lower_b,higher_b+1):
	if x%5 ==0:
		list_5.append(x)
	if x%7==0:
		list_7.append(x)
	if x%5==0 and x%7==0:
		list_35.append(x)
	x=x+1

print("\nNumbers divisible by 5 are:",list_5)
print("\nNumbers divisible by 7 are:",list_7)
print("\nNumbers divisible by both 5 & 7 are:",list_35)
print("\nEnd of Code\n")


#######################################################
#Code -2: 2+22+222+2222+................n##############
#######################################################
print()
n= int(input("Enter the number of terms:"))
sum_c =0

for i in range(1,n+1):
	 for j in range(0,i):
		 sum_c = sum_c+2*10**j
		 j = j+1
	 i= i+1
print("the sum =",sum_c)
print("End of Code\n")

# #######################################################
# #Code -3: Add numbers till user quits ##############
# #######################################################
print()
s1=0
i= 'p'
while(i!='q'):
	 print ("Enter the number you want to add or else press 'q' to quit")
	 i = input ()
	 if (i == 'q'):
		 break
	 else:
		 s1 = s1+ int(i)

print("Sum of the numbers input = {}.".format(s1))
print("\nEnd of Code\n")

# #######################################################
# #Code -4: Calculate factorial##############
# #######################################################
print()
n= int(input("Enter the numberto calculate facorial:"))
factorial =1
i = n
while (i > 0):
	 factorial = factorial * i
	 i=i-1

print("The factorial of {} = {}".format(n, factorial))
print("End of Code\n")

#######################################################
#Code -5: Calculate factorial##############
#######################################################
print()
s1 = "python language is best programming language"


i = 0
while (i< len(s1)-1):

	 if (s1[i+1]!=' ' and i%2== 0):
	 	 print(s1[i].upper(), end = '-')
	 elif (s1[i+1]!=' ' and i%2!= 0):
	 	 print(s1[i].lower(), end = '-')
	 elif (s1[i+1]==' ' and i%2== 0):
 	 	 print(s1[i].upper(), end = ' ')
 	 	 i+=1
	 elif (s1[i+1]==' ' and i%2!= 0):
	 	 print(s1[i].lower(), end = ' ')
	 	 i+=1
	 i+=1
if ((len(s1)-1)%2== 0):
	 print(s1[i].upper())
else:
	 print(s1[i].lower())
	
print("\nEnd of Code\n")

