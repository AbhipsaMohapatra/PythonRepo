# Q1
def power(x,n):
    if(n==0):
        return 1
    elif(n==1):
        return x
    if(n%2==0):
        return power(x*x,(n//2))
    else:
        return x*power(x*x,(n//2))
print(power(2,4))    

def gcd(x,y):
    if(y==0):
        return x
    return gcd(y,x%y)
print(gcd(3,6))

def printD(n):
    if(n==0):
        return
    printD(n-1)
    print(n,end=" ")
printD(5)


    
    
