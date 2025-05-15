'''def nufrom12(n):
    if n == 0:
        print("stopped")  # Base case
    else:
        print(n)
        nufrom12(n - 1)  # Recursive call only moves toward 0

# ✅ Call it ONCE here to start
nufrom12(12)



def num5bellow(l)

    if l==0:
        print("hello")

        else
        print(l)
        num5bellow(l-1)


num5bellow(5) :

def factorial(n):#this i think just like  fuction how we define them and they have partameters .. so we need todefine this and the parameter we have is
    #is n . then this valie of n is what will be using ..
    if n == 0:#so when the program reaches to the point where it is at n==0 it brings one as a result or what? cause other taht we were working with before were printing a certain value
        return 1#so this is the base case .. when program reaches here it stops the recursion
    return n * factorial(n - 1)#is this where recursion happens
#should nwe be having an else statement ..or this on is different ?
# Test it
print(factorial(5))  # Output: 120we now call ir and the code is executed .. n takes value of 5 and the code is executed
#based on the code we placed in our program


#let me try on e

def sumofnumbers(n):
    if n==0 :
       return 0
    else:
        return n+ sumofnumbers(n-1)



def reverse_string(s):# this is the fast part defining our function and adding s parameter
    # Base case: if the string is empty, return it
    if s == "":
        return s#base case sp that when the value of s beocmes empty no more curacters to reverse returns itself
    else:
        # Recursive case: last character + reversed remaining string
        return reverse_string(s[1:]) + s[0]#logical part where decisons are made on what will happen on code

# Test the function
print(reverse_string("paulkiragu"))  # Output: "olleh"

def countdown(n):
    if n == 0:
        return 0
    else:
       print(n)
       (countdown(n - 1))
#we use return when we want a particulr output maybe sum etc .. but if we want to see values we use print output
print(countdown(9))  # ✅ Now it's correctly placed





def sumofnumbers(n):
    if n==0:
        return 0
    else:
      return n+sumofnumbers(n-1)
print(sumofnumbers(5))


def factorialofnum(n):
    if n==0:
        return 1
    else:
        return n*factorialofnum(n-1)
print(factorialofnum(20))
so far i know about recursion in .. factorial . sum of numbers .. reversing a string ... countdown


def checkevenorodd(n):
    if n%2==0:
        print("even")
    else :
        print("odd")

checkevenorodd(19)


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

# Test
print(sum_of_digits(1234))  # Output: 10


def trialf():#a function is a thing gtaht we declare and we give it code that should run whern we call
    #the function .. the excecutable code
    print("hii there")

print(trialf())

def sumfunction():
    print(5+3)


sumfunction()

#check on functions args etc .. tommorrow data structures setd=s dictionaries , tuples ,strings etc and aplication'
#in code
#an example for a function
def newfunction():
    print(4+3)

print(newfunction())








#data structures .. and the differentg functionalities .. how they work in code
#some examples tuples dictionaries . sets etc . we have to know the right data type to  use on order to optimize
#the algorithms -- different data tyoes have different functionalities and handle different values . so we also
# have to check what is our system handling .. what is the kind of ddata we are suing and what is the best data types to use in outr
#in our algorithms to optimize it performance .. an algorothm a set of instruction to do a particular thing

#sets
number=[2,4,5,3]
print(number[0])#this is trying to acess a particular valie in a set

number[2]=5#this is assighning values to a certain index of a set
print(number[2])

#tuples
student=("paul","kiragu"),5,8,3#defining values of the tuples
print(student)
print(student[1])# this is trying to print object in a particular index

#dictionaries
#using the various data types and fuctionalities .. adding values
#removing values etc

# Creating a dictionary
student = { "name": "John", "age": 21,
"grades": [88, 92, 79] }
#in dictonaires the ey must have a coresponding values that show their values
# Accessing a value
#print(student["name"])
student["name"]=35#chaangi corresponding values
del student["grades"]#to remove values
print(student["name"])
print(student)

#sets operations
numbers={3,4,5,"orange","lemons","juice"}
print(numbers)

numbers.add("apple")
numbers.discard("orange")
print(numbers)



#stack .. forst in first out .. different types of stacks
#que .. a particular order if followed .. fist to come in the firs to come out
#diffenrent types of ques reverse que etc .. advantages and disadvantages of ]
of either in code

'''