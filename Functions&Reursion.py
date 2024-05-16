#Function defination
def calc_sum(a,b): #parameters
    return a + b

sum = calc_sum(178,258)  #function call ; arguments
print(sum)

#average of 3 numbers
def calc_avg(a,b,c) :
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
calc_avg(98,97,99)



#default parameters
def calc_prod(a,b=2) :
    print (a*b)
    return a*b
                     
calc_prod(1)


#practise Q1
cites = ["delhi","gurgaon","bengaluru","pune","mumbai","kashmir"]
heroes = ["ironman","shaktiman","hulk","captain america"]
def print_len(list):
    
    print(len(list))

print_len(cites)
print_len(heroes)


#Q2
heroes = ["ironman","shaktiman","hulk","captain america"]

def print_len(list) :
    print(len(list))

def print_list(list) :
    for item in list :
        print(item, end=" ")

print_list(heroes)


#Q3
n = 5
def cal_fact(n) :
    fact = 1
    for i in range (1,n+1) :
        fact *= i
        print(fact)
cal_fact(5)


#Q4
def converter(usd_val) :
    inr_val = usd_val * 83
    print(usd_val,"USD =",inr_val,"INR")

converter(5)


#Recursion Function

def show(n) :
    if(n == 0):  #Base case
        return
    print(n)
    show(n-1)
show(5)  #5, 4 =n-1, 3 =n-2, 2 = n-3, 1

