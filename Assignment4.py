#Assignment 4
#Q1
import sys
"""import random

n = int(input("Enter the value of n"))
l=[]
for i in range(0,n):
    l.append(random.randint(1,n))
s= sum(l)
print(f"The sum of elements is {s}, the avg is {s/n}")
print(l)"""


#Q2
"""def rotate(a,b,c):
    t=tuple()
    
    t=t+(c,a,b)
    return t
a="Doug"
b=22
c=1984
a,b,c=rotate(a,b,c)
print(f" first call a= {a} b={b} c={c}")
a,b,c=rotate(a,b,c)
print(f" second call a= {a} b={b} c={c}")
a,b,c=rotate(a,b,c)
print(f" third call a= {a} b={b} c={c}")"""


l=[]
while(True):
    option = input("Enter c/C for create d/D for display i/I for insert del/Del for delete  and (exit) for exit")
    match(option.lower()):
        case "c":
            
            
            n = int(input("Enter the value of n"))
            for i in range(0,n):
                l.append(int(input("Enter number")))
                
        
        case "d":
                         
             print(l)

        case "i":
             ele = int(input("Enter the element"))
             ind = int(input("Enter the position"))
             l.insert(ind,ele)
                         
        case "del":
            #ele = int(input("Enter the element"))
            ind = int(input("Enter the position"))
            del l[ind]
        case "exit":
            sys.exit(0)
                         
                         
              

                


