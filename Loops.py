count = 1
while count <=5 :
    print("hello")
    count = count +1 
    print(count)

i = 1
while i<=9 :
    print("itvedant")
    i+=1

#practice Q1
num = 1
while  num<=100 :
    print(num)
    num+=1

#Q2
num = 100
while num >=1 :  #stopping condition
    print(num)
    num-=1

#Q3
    #n = int(input("enter any number  :"))
    #num = 1
    #while num <=10 :
     #   print(n*num)
      #  num += 1



#Q4
nums = (1,4,9,16,25,36,49,64,81,100,36)
i = 0
x = 36
while i < len(nums) :
     if(nums[i] == x) :
          print("found at index",i)
     else :
         print("finding...")
     i += 1  

#break loop
i = 1
while i <= 5 :
    if(i == 3) :
        break
    i += 1
    print(i)
    print ("end of loop")

# continue
    i = 0
    while i <= 10 :
        if(i%2 != 0) :
            i += 1
            continue  #skip 
        print(i)
        i += 1

#for
        nums = [1,2,3,4,6,7,8,9,10]
        for val in nums :
            print(val)

#practice Q1
nums = [1,4,9,16,25,36,49,64,81,100]
for ele in nums :
    print(ele)

#Q2
nums = (1,4,9,16,25,36,49,64,81,100,49)
i = 0
x = 49
for el in nums :
    if (el == x) :
       print("found at indx" ,i)
    i += 1

#range
    for i in range(10) : #range(stop)
        print(i)


for i in range(2,10) : #range(start,stop)
        print(i)


for i in range(2,10,2) : #range(start,stop,step)
        print(i)

#practice Q1
        for i in range(1,101):
             print(i)

#Q2
        for i in range(100,0, -1):
            print(i)


#Q3
n =  int(input("enter number  :"))
for i in range(1,11) :
            print(i*n)


#pass
for i in range(100,0, -1):
     pass

#practice Q1

n = 7
sum = 0
i = 1
while i <=n :
    sum += i
    i += 1
    print("total some :",sum)


#Q2
n = 7
facto = 1
i = 1
while i <=n :
    facto *= i
    i += 1
    print("factorial :",facto)
    

   