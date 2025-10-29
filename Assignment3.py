#Assignmnt3

#Q1
"""def maxVal(a,n):
   l=[]

   while(a>0):
      d=a%10
        
      l.append(d)
      a=a//10
   ans=[]
   if(n>len(ans)):
       return "cannot find more nums"
   for i in range(n):
      p=max(l)
      ans.append(p)
      l.remove(p)
   return ans    

a=int(input("Enter a number"))
n=int(input("Enter the number of maximums you want to find"))

print(maxVal(a,n))"""


"""#Q2
def find(n1,n2):
    for i in range(n1,n2+1):
        if(i%3==0 and i%5==0):
            print(i,end=",")
find(100,500)"""

"""#Q3
def Q3(n1,n2):
    sum=0
    for i in range(n1,n2+1):
        if(i%2==0):
            sum+=i**2
    return sum
print("The sum is ",Q3(1,50))"""

#Q4
"""def Q4(s):
    return s[::-1]
s= input("Enter a string ")
print("The reversed string is ,",Q4(s))"""

#Q5
"""def nod(n):
    digits=0
    while(n>0):
        d=n%10
        digits+=1
        n=n//10
    return digits
val= int(input("Enter the number "))
print(f"The no. of strings in {val} is {nod(val)} ")"""

#Q6
"""def palindrome(s):
    return s == s[::-1]
val= input("Enter the String ")
print(f"The given input is a palindrome ,{palindrome(val)}")"""

#Q7
"""def checkAlpha(a):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    if( a in vowels):
        return "Alphabet"
    else:
        return "Not an Alphabet"

val= input("Enter the number ")
print(f" {val} is {checkAlpha(val)} ")"""

#Q8
"""def findMonth(mon):
    months= {"January":31,"Feb":"28/29","March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"Sept":30,"October":31,"November":30,"December":31}
    return months[mon]
mon = input("enter a month ")
print(f" {mon} has {findMonth(mon.capitalize())} days ")"""

#Q9

#Q10
"""string = input("Enter a string").strip();
ans=[]
def recurse"""
    



#11


"""string = input("Enter a string").strip();
d = {}
c=0
for ch in string:
    if(ch not in d):
        d[ch] = string.count(ch)

for i,j in d.items():
    if(j%2!=0):
        c+=1
    if(c>1):
        print("Not a palindrome")
        break
else:
    print("Can form a palindrome")"""


#14
"""a = int(input("Enter the integer"))
val=a
l = len(str(a))
sum =0
while(a>0):
    d=a%10
    sum+=d**l
    
    a=a//10
print(sum==val)"""




