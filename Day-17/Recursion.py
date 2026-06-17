

#Recursion


def func():
    if basecondition:
        return
    func()





#5 to 1
def func(num):
    if num==0:
        return
    print(num,end=' ')
    func(num-1)
func(5)






#1 to 5
def func(num):
    if num==0:
        return
    func(num-1)
    print(num,end=' ')
func(5)







#Sum of digits
def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))







#Factorial
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))








#Power
def power(base,pow):
    if pow==0:
        return 1
    return base * power(base,pow-1)
print(power(2,4))
print(power(3,3))







#Reverse str
def reversestr(s,ind):
    if ind==0:
        return s[0]
    return s[ind]+reversestr(s,ind-1)
l="Python Programming"
print(reversestr(l,len(l)-1))
