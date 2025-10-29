#print("Name : Abhipsa Mohapatra")
#print("Address : 38 Pawani Conplex , Jagmohannagar Khandagiri,Bhubaneswar")
import math

#Q2
"""name=input("Enter your name")
print("Hello",name)"""

#Q3

"""length = float(input("Enter Length"))
bredth = float(input("Enter Bredth"))

ans = length*bredth
print("The area of the room is ",ans)"""

#5

"""val1 = float(input("Enter the value 1 "))
val2 = float(input("Enter container 2 "))


print("The value of refund is $%.2f" % (val1 * 0.10 + val2 * 0.25))"""

#7
"""n = int(input("Enter Number "))
ans = (n*(n+1))/2
print("The sum of ",n,"numbers is ",ans)"""

#11
"""n= 2
val = n**3+2*n**2+3*n+4
print("P(expression) =",val)"""

#12
"""r = float(input("Enter the value of radius "))
area = math.pi*r*r
volume = (4/3)*math.pi*(r**3)
print("Area ",area," Volume is ",volume)"""

#25
"""days = int(input("Enter number of days "))
hours = int(input("Enter the number of hours "))
minutes  =int(input("Entr the minutes "))
seconds = int(input("Enter the numbr of seconds "))

ans = days*24*3600+hours*3600+minutes*60+seconds
print(days," days ",hours," hours ",minutes," minutes ",seconds," seconds is ",ans," seconds")"""

secs = int(input("Enter the number of seconds"))
days = secs//(24*3600)
hour = (secs-days*24*3600)//(3600)
mins =  (secs-(hour*3600+days*24*3600))//60
seconds =  (secs-(mins*60+hour*3600+days*24*3600))
print("%.2f",days,":","%.2f",hour,":","%.2f:",mins,":","%.2f:",seconds)


