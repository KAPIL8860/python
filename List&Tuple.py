#List
student = ["karan",95.7,88,"delhi"]
print(student)

#List Method
list = [2,1,3]
list.append(4) #append
print(list)

list = [2,1,3]
print(list.append(4))
print( list.sort()) #ascending order
print(list)

list = ["banana","litchi","apple"]
print( list.sort(reverse=True)) #descending order
print(list)

list = ['a','f','c','d','e','b']
list.reverse()
print(list)

list = [2,1,3]
list.insert(1,5)
print(list)

#Tuple
tup = (2,3,6)
print(type(tup))

#Tuple Method
tup = [1,2,3,4]
print(tup.index(2))  #returns index of first occurrence

tup = [1,2,3,4,2,2,2]
print(tup.count(2))  #counts total occurrence

#lets practice Q1
movies = []
mov1 = input("enter first movie :")
mov2 = input("enter second movie :")
mov3 = input("enter third movie :")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#Q2
list1 = [1,2,1]
list2 = [1,2,3]

copy_list = list1.copy
copy_list = list1.reverse

if (copy_list == list1):
    print("palindrom")
else :
    print("not palindrom")

#Q3
grade = ("c","d","a","a","b","b","a")
print(grade.count("a"))

#Q4
grade = ["c","d","a","a","b","b","a"]
print(grade.sort())
print(grade)