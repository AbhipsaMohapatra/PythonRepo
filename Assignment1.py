#Q2
class Bank:
    def __init__(self,amount):
        self.amount=amount
    def withdraw(self,amt):
        data=self.amount-amt
        if(data<0):
            print("Amount cannnt be withdrawn")
        else:
            self.amount=data
            print("Amount withdawn successfully ",self.amount)
            
    def deposit(self,amt):
        if(amt<0):
           print("please enter a valid deposit")
        else:
            self.amount+=amt
            print("Amount deposited successfully ",self.amount)
b1 = Bank(2000)
b1.deposit(1000)
b1.withdraw(2000)


# Q3
class Chapter:
    def __init__(self,title,pc):
        self.title=title
        self.pc=pc
class Book:
    def __init__(self,chapters):
        self.chapters=chapters

    def getTotalPage(self):
        totalPc=0
        for i in self.chapters:
            totalPc+=i.pc
        return totalPc
ch1=Chapter("The wind and sun",123)
ch2=Chapter("You can win",200)
ch3 = Chapter("With Love",300)
b = Book([ch1,ch2,ch3])
print("The total page is ",b.getTotalPage())


#Q5
class Time:
    def __init__(self, time_str):
        self.time_str = time_str

    def is_valid(self):
        parts = self.time_str.split(":")

        
        if len(parts) != 3:
            return False, "Invalid format! Use HH:MM:SS"

        try:
            hh, mm, ss = map(int, parts)
        except ValueError:
            return False, "Time must contain only numbers!"

        
        if not (0 <= hh <= 23):
            return False, "Hour must be between 00 and 23"
        if not (0 <= mm <= 59):
            return False, "Minute must be between 00 and 59"
        if not (0 <= ss <= 59):
            return False, "Second must be between 00 and 59"

        return True, "Valid time"

    def convert12Hr(self):
        valid, message = self.is_valid()
        if not valid:
            return message

        hh, mm, ss = map(int, self.time_str.split(":"))

        period = "AM"
        if hh >= 12:
            period = "PM"

        
        if hh == 0:
            hh = 12
        elif hh > 12:
            hh -= 12

        return f"{hh:02d}:{mm:02d}:{ss:02d} {period}"


time_input = input("Enter time (HH:MM:SS): ")
t = Time(time_input)

valid, msg = t.is_valid()
if valid:
    print("12-hour format:", t.convert12Hr())
else:
    print("Error:", msg)


# Q6

class BankAccount:
    def __init__(self,accId,balance):
        self.__accId=accId
        self.__balance=balance
    def withdraw(self,amt):
        data=self.__balance-amt
        if(data<0):
            print("Amount cannnt be withdrawn")
        else:
            self.__balance=data
            print("Amount withdawn successfully total amount after withdraw ",self.__balance)
            
    def deposit(self,amt):
        if(amt<0):
           print("please enter a valid deposit")
        else:
            self.__balance+=amt
            print("Amount deposited successfully total amount after deposit ",self.__balance)
        
        
            
b1 = BankAccount(123,2340)
print(b1.withdraw(120))
print(b1.deposit(1200))


# Q7
class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value;
    def __str__(self):
        
class Deck:
    pass
class Player:
    pass



#Q8
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def display_info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self,make,model,num_doors):
        super().__init__(make,model);
        self.num_doors=num_doors
    def display_info(self):
        return f"{self.make} {self.model} {self.num_doors}"
        


v=Vehicle(1987,"Honda")
c=Car(1987,"Honda",4)
print(c.display_info())
print(v.display_info())


#Q9

class Shape:
    def area():
        pass
class Rectangle(Shape):

    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth

    def area(self):
        return self.length*self.bredth
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7)*self.radius*self.radius
r=Rectangle(3.0,2.0)
c=Circle(7)
print(r.area())
print(c.area())

#Q11


class Dog():
    def speak(self):
        print("The Dog Barks")
class Robot():
    def speak(self):
        print("The Robot makes sound")
def describe(d,r):
    d.speak()
    r.speak()

d=Dog()
r=Robot()
describe(d,r)

#Q18
import pandas as pd
import matplotlib.pyplot as plt
c=[12,34,67,78]
f=(list(map(lambda e:(273.15+e),c)))

df=pd.DataFrame({"celcius":c,"Kelvin":f})
print(df)

plt.plot(c,f)
plt.xlabel("celcius")
plt.ylabel("Kelvin")

plt.title("Celcius to kelvin")
plt.show()
        



    
