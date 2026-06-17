




#Local Access
def display():
    n=10
    print("Inside:",n)
display()





#Global Access
n=10
def display():
    print("Inside:",n)
display()
print("Outside:",n)
    




#Inside Global access
def display():
    global n
    n=10
    print("Inside:",n)
display()
print("Outside:",n)
    





def display():
    global n
    n+=10
    print("Inside:",n)
n=10
display()
print("Outside:",n)
    






#Inner Fun
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()
    print("Outer function:",n)
outer()







#Scope Loss
s='Python'
print(len(s))
len=5
print(len(s))






#Pass by Value
---> int,float,complex,str,tuple,bool





#int
def update(n):
    n+=10
    print("Inside:",n)
n=10
update(n)
print("Outerside:",n)





#float
def update(n):
    n+=10
    print("Inside:",n)
n=10.4
update(n)
print("Outerside:",n)







#complex
def update(n):
    n+=10
    print("Inside:",n)
n=3+4j
update(n)
print("Outerside:",n)






#string
def update(n):
    n+="lang"
    print("Inside:",n)
n="Python"
update(n)
print("Outerside:",n)






#Tuple
def update(n):
    n+=(6,7)
    print("Inside:",n)
n=(1,2,3,4,5)
update(n)
print("Outerside:",n)





#Bool
def update(n):
    n+=False
    print("Inside:",n)
n=True
update(n)
print("Outerside:",n)





#Pass by Reference

#List
def update(n):
    n+=[5,6]
    print("Inside:",n)
n=[1,2,3,4]
update(n)
print("Outerside:",n)






def update(n):
    n+=10
    print("Inside:",n)
n=10
update(n)
print("Outerside:",n)

