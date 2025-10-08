#Assignment2
from math import sqrt
import sys
import statistics
#Q1
"""rain= input("Is it raining (yes/no)")
if(rain.lower()=="yes"):
    print("Carry an umbrella")
else:
    print("Bye")"""
    
#Q2
"""rain= input("Is it raining (yes/no)")
if(rain.lower()=="yes"):
    print("Carry an umbrella")
elif(rain.lower()=="no"):
    print("No need to carry an umbrella")
else:
    print("Bye")"""

#Q3
"""val = float(input("Enter your score"))
if(val>100 or val<0):
    print("Ennter the marks correctly")
    
else:
   if(val>=90):
    print("A:Excellent")
   elif(val>=80):
    print("B:Good")
   elif(val>=79):
    print("C:Average")
   elif(val>=69):
    print("D:Needs Imporvement")
   else:
    print("F:Fail")"""

#Q4
"""val = int(input("Enter a number"))
if(val%2==0):
    print(val," is Even number ")
else:
    print(val," is odd number")"""

#Q5
"""year = int(input("Enter a year"))

if(year%4==0 or (year%100==0 and year%400==0)):
    print(year," is a leap year")
    
else:
    print(year," is not a leap year")"""

#Q6
"""num = int(input("Enter a number "))
j=2
while(j<=sqrt(num)):
    if(num%j==0):
        print(" Not Prime")
        break
    j=j+1
else:
    print("Prime")"""

#Q7

"""num = int(input("Enter a number "))
sum=0
for i in range(2,num):
    j=2
    flag = True
    while(j<=sqrt(i)):
        if(i%j==0):
            flag=False
            break
        j=j+1
    if(flag):
        sum=sum+i
print("The sum of all prime numbers lessa than ",num," is ",sum)"""




#25
"""for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print("")"""

#8
"""while(True):
    val = int(input("Enter a number"))
    if(val>0):
        if(val%2==0):
            print("You got an even number ",val*2)
            break
        else:
            print("You got an odd number ",val*val)
            break"""
        
        
#25
"""for i in range(4):
    for j in range(4,i,-1):
        
        print(" ",end=" ")
        
    
    

    for j in range(i+1):
        print("*",end=" ")
    print("")  """

"""for i in range(4):
    for j in range(i+1):
        print(" ",end=" ")

    for k in range(4,i,-1):
        print("*",end=" ")
    print("")   """

#9
"""val =int(input("Enter a number"))
if(val<0):
    print("Invalid Input")
    sys.exit(1)
ans = val%5

match(ans):
    case 0:
        print("The remainder of ",val," and 5 is 0")
    case 1:
         print("The remainder of ",val," and 5 is 1")
    case 2:
         print("The remainder of ",val," and 5 is 2")
    case 3:
         print("The remainder of ",val," and 5 is 3")
    case 4:
         print("The remainder of ",val," and 5 is 4")"""

#10
"""str = input("Enter a string ")

for i in range(len(str)):
    st=""
    for j in range(i,len(str)):
        st+=str[j]
        print(st,end=" ")"""

#11
"""while(True):
    a = int(input(" Enter num1 "))
    b = int(input(" Enter num2 "))
    op = input("Enter an operator from (+,-,*,/)");
    if(op.strip()[0]=='+'):
        print(" The sum of ",a," and ",b," is ",(a+b))
    elif(op.strip()[0]=='-'):
         print(" The  diff of ",a," and ",b," is ",(a-b))
    elif(op.strip()[0]=='*'):
         print(" The  prod of ",a," and ",b," is ",(a*b))
    elif(op.strip()[0]=='/'):
         q= (a/b) if b!=0 else "Division by Zero is not possible"
         print(" The  quotient of ",a," and ",b," is ",q)
    else:
        print("Invalid operato")
    b= input(" Do you want to exit (Enter Exit or else no) ")
    if(b.strip().lower()=='exit'):
        print("Thanks")
        break
"""

#12
"""l = [1,2,3,2,3,4,4,4,5,4,5,6]
print(statistics.mean(l)," is the mean ")
print(statistics.mode(l)," is the mode ")
print(statistics.median(l)," is the median is ")"""

#13
"""row = int(input("Enter Row "))
col = input("Enter col (a-h) ")
colI = ord(col[0])-ord('a')

if((row%2==0 and colI%2==0) or (row%2!=0 and colI%2!=0)):
    print("white")
else:
    print("black")"""

#15
val = int(input("Enter the number "))
i=1
sum =0
while(i<val):
    if(val%i==0):
        sum+=i
        print(i)
    i=i+1    
if(sum==val):
    print("Perfect Number")
else:
    print("Not a perfect number ")
        
    



        
        
        
        
        


    
    


          
    
     
    
    
    

    
