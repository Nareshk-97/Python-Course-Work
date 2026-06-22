#Built-in Module

import sys

print(sys.argv)
print(sys.path)
print(sys.version)

print("Before exit")
sys.exit()
print("After exit")


#
import platform
print(platform.system(),platform.release(),platform.processor())




#math
import math

print(math.pi)
print(math.e)

print(math.sqrt(25))
print(math.pow(2,5))

print(math.ceil(12.3))
print(math.ceil(12.00000001))
print(math.ceil(12.99999999))
print(math.ceil(12.8))

print(math.floor(12.3))
print(math.floor(12.000000001))
print(math.floor(12.99999999))
print(math.floor(12.8))



#
import math

print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(8,28))

print(math.log(10,10))

print(math.sin(10))
print(math.cos(10))
print(math.tan(10))

print(math.degrees(20))
print(math.radians(20))




#random
import random

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l=['python','c','c++','java','html']
print(random.choice(l))
print(random.choices(l,k=3))

s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)




#
import random

random.seed(9)
print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l=['python','c','c++','java','html']
print(random.choice(l))
print(random.choices(l,k=3))

s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)





#Collections
#Counter
import collections

s='Python Programming Language'
print(collections.Counter(s))

d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d





#Defaultdict

import collections
s='Python Programming Language'
d=collections.defaultdict(int)
for i in s:
    d[i]+=1
print(d)



#deque
import collections

l=collections.deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop
print(l)




import itertools

print(list(itertools.combinations('abcd',2)))
print(list(itertools.permutations('abcd',2)))



#
from itertools import combinations,permutations

com=combinations('abcd',2)
print([''.join(i) for i in com])

per=permutations('abcd',2)
print([''.join(i) for i in per])
