# arithmetic operators
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #a^b

# relational operators
a = 50
b = 20

print(a == b) #false
print(a != b) #true
print(a >= b) #true
print(a >  b) #true
print(a <= b) #false
print(a <  b) #false

#assignment operators 
num = 10
#num = num + 10    #10+10 => 20
num += 10
print("num :", num)


#logical operators
a = 50
b = 30
print(not False)
print(not (a>b))

val1 = True
val2 = True
print("and operator :",val1 and val2)
print("or operator :",val1 or val2)

#type conversion
a = float("2")
b = 4.25

print(type(a))
print(a + b)

#input
name = input("enter your name :")
age = input("enter your age:")
marks = input("enter your marks:")

print("welcome",name)
print("age=",age)
print("marks=",marks)

#practice Q1
first = int(input("enter first :"))
second = int(input("enter second :"))

print("sum=",first+second)

#Q2
side = float(input("enter square side :"))

print("area=", side * side)

#Q3
a = float(input("enter first :"))
b = float(input("enter second :"))

print("avg=", (a+b)/2)

#Q4
a = int(input("enter first :"))
b = int(input("enter second :"))

print(a>=b)