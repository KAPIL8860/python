#Dictonary
info = {
    "name" : "itvedant",
    "subjects" : ["python","c","java"],
    "topics" : ("dict","set"),
    "age" : 35,
    "is_adult" : True,
    12.99 : 99.4
}

info ["name"] = "kapil"  #overwrite
info["surname"] = "kumar"
print(info)
print(type(info))




#nested dictionary
student = {
    "name" : "kapil",
    "subjects" : {
        "phy" : 97,
        "che" : 85,
        "math" : 85
    }
}
print(student)




#Dictionary method
student = {
    "name" : "kapil",
    "subjects" : {
        "phy" : 97,
        "che" : 85,
        "math" : 85
    }
}
print(student.keys())  #returns all keys


student = {
    "name" : "kapil",
    "subjects" : {
        "phy" : 97,
        "che" : 85,
        "math" : 85
    }
}
print(student.values())  #returns all value

student = {
    "name" : "kapil",
    "subjects" : {
        "phy" : 97,
        "che" : 85,
        "math" : 85
    }
}
print(student.items()) #returns all (key,value) pairs as tuple

student = {
    "name" : "kapil",
    "subjects" : {
        "phy" : 97,
        "che" : 85,
        "math" : 85
    }
}
print(student.get("name"))  #returns the key according to value

student = {
    "name" : "kapil",
    "subjects" : {
        "phy" : 97,
        "che" : 85,
        "math" : 85
    }
}

new_dict = {"city" : "delhi","age" : 18}
student.update(new_dict)
print(student)  #insert the specified items to the dictionary




#set
collection = {1,2,3,2,2,"hello","hello","world"}
print(collection)
print(type(collection))




#empty set; syntax
collection = set()

print(type(collection))




#set methods
collection = set()

collection.add(1) #add new value
collection.add(2)
collection.add("itvedant")

print(collection)

collection = {"python","itvedant","youtube","javascript"}
print(collection.pop())
print(collection.pop()) #returns random value


set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))  #{1,2,3,4}


set1 = {1,2,3}
set2 = {2,3,4}
print(set1.intersection(set2))  #{2,3}




#practice Q1
dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of facts & figures"]
}
print(dictionary)




#Q2
subjects = {
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(subjects)
print(len(subjects))





#Q3
marks = {}

x = int(input("enter phy :"))
marks.update({"phy" :x })

x = int(input("enter chem :"))
marks.update({"chem" :x })

x = int(input("enter math :"))
marks.update({"math" :x })

print(marks)




#Q4
marks = {9,"9.0"}
print(marks)

