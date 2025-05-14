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
'''
def sumfunction():
    print(5+3)


sumfunction()

#check on functions args etc .. tommorrow data structures setd=s dictionaries , tuples ,strings etc and aplication'
#in code
