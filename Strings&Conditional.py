str1 = "this is a string.\nwe are creating it in python."
print(str1)

str2 = "kapil"
len1 =(len(str2))
print (len1)
str3 = "kumar"
len2 =(len(str3))
print (len2)
final_str = str2+str3
print(final_str)



str7 = "hello world"
print(str7[:4]) #[0:4]
print(str7[:4]) #[5:len(str7)]


str8 = "i am studying python from itvedant"
print(str8.endswith("nt"))  #returns true is string ends with substr

str9 = "i am studying python from itvedant"
str9 =str9.capitalize()  #capitalizes 1st char
print(str9)

str10 = "i am studying python from itvedant"
print (str10.replace("python","javascript")) #replace all occurrences of old

str11 = "i am studying python from itvedant"
print (str11.find("from")) #returns 1st index of 1st occurrer

str12 = "i am studying python from itvedant"
print (str12.count("a")) #counts the occurrences of substr

#lets practice Q1
name =input("first name :") 
print ("lenth of your name is", len(name))

#Q2
str16 = "hi$ am$ the $ symbol $99.99"
print(str16.count("$"))


# conditional statments
age = 14

if (age>=18):
    print("can vote")  #indentation
else:
    print("cannot vote")

marks = int(input("enter student marks :"))

if (marks >=90):
    grade = "a"
elif (marks >=80 and marks <90):
    grade = "b"
elif (marks >=70 and marks <80):
    grade = "c"
else:
    grade = "d"

print("grade of the student ->", grade)

# nesting
age = 32
if (age>=18):
    if (age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

# practice Q1
num = int(input("enter the number :"))

if(num % 2 == 0):
    print ("even")
else:
    print("odd")

#Q2
a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
c = int(input("enter the third number :"))

if (a>=b and a>=c):
    print("first number is largest",a)
elif(b>=c):
    print("second number is largest",b)
else:
    print("third number is largest",c)

#Q3
x = int(input("enter the number :"))
if (x % 7 == 0):
    print("multiple of 7")
else:
    print("not multiple of 7")

