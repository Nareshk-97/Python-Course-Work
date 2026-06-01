Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name=input("Enter your name:")
Enter your name:naresh
name
'naresh'
age=input("Enter your age:")
Enter your age:21
age
'21'
type(age)
<class 'str'>
gpa=float("Enter the cpa:")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    gpa=float("Enter the cpa:")
ValueError: could not convert string to float: 'Enter the cpa:'
gpa=float(input("ENter the cpa:")







gpa=float(input("ENter the cpa:")
          
SyntaxError: invalid syntax. Perhaps you forgot a comma?
gpa=float(input("ENter the cpa:"))
          
ENter the cpa:7.8
gpa
          
7.8
type(gpa)
          
<class 'float'>
'naresh ajay akhil virat dhoni'
          
'naresh ajay akhil virat dhoni'
'naresh ajay akhil virat dhoni'
          
'naresh ajay akhil virat dhoni'
'naresh ajay akhil virat dhoni'.split(' ')
          
['naresh', 'ajay', 'akhil', 'virat', 'dhoni']
names=input("Enter the names:").split()
          
Enter the names:naresh ajay akhil virat dhoni\
names
          
['naresh', 'ajay', 'akhil', 'virat', 'dhoni\\']
products=input("ENter the prodects:").split()
          
ENter the prodects:lap mouse key pen
prodects
          
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    prodects
NameError: name 'prodects' is not defined. Did you mean: 'products'?
products
          
['lap', 'mouse', 'key', 'pen']
topics=tuple(input("Enter the topics:").split())
          
Enter the topics:token statement variable comments
topics
          
('token', 'statement', 'variable', 'comments')
op=set(input("Enter the oper:").split())
          
Enter the oper:in not in is is not and or not
op
          
{'or', 'is', 'and', 'not', 'in'}
marks=input("Enter the marks:").split()
          
Enter the marks:12 20 30 40 50 
marks
          
['12', '20', '30', '40', '50']
map(int,input("Enter the marks:").split())
          
Enter the marks:1 2 34 56 78 
<map object at 0x00000223A1087F70>
list(map(int,input("Enter the marks:").split()))
          
Enter the marks:1 2 3 4 5 6
[1, 2, 3, 4, 5, 6]

prices=tuple(map(int,input("Enter the prices:").split()))
          
Enter the prices:1 2 3 4 5 6
prices
          
(1, 2, 3, 4, 5, 6)
rating=set(map(int,input("Enter the rating:").split()))
          
Enter the rating:4 3 4 5 2 3 5 
rating
          
{2, 3, 4, 5}
per=list(map(float,input("Enter the per's:").split()))
          
Enter the per's:56.3 45.3 54.3 56.9 87.5
per
          
[56.3, 45.3, 54.3, 56.9, 87.5]
prices=tuple(map(float,input("Enter the prices:").split()))
          
Enter the prices:434 64 78 964 467 
prices
          
(434.0, 64.0, 78.0, 964.0, 467.0)
prices=set(map(float,input("Enter the prices:").split()))
          
Enter the prices:325 734 668 24 975
prices
          
{325.0, 975.0, 24.0, 668.0, 734.0}

username,password=input("Enter the username & password:").split()
          
Enter the username & password:naresh N@123
username
          
'naresh'
password
          
'N@123'
a,b,c,d=list(map(int,input("Enter the 4 sides:").split()))
          
Enter the 4 sides:2 3 4 5
a
          
2
b
          
3
c
          
4
d
          
5
price,discount=list(map(float,input().split()))
          
price,discount=list(map(float,input().split()))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    price,discount=list(map(float,input().split()))
ValueError: could not convert string to float: 'price,discount=list(map(float,input().split()))'
price,discount=list(map(float,input().split()))
          
472346 49.0
price
          
472346.0
discount
          
49.0
a=eval(input())
          
2455
a
          
2455
a=eval(input())
          
2457.744
a
          
2457.744
a=eval(input())
          
[1,2,3,4,5]
a
          
[1, 2, 3, 4, 5]
a=eval(input())
          
{1,2,3,4}
a
          
{1, 2, 3, 4}
type(a)
          
<class 'set'>
#string Operations
          
s="python programming lang"
          
s
          
'python programming lang'
type(s)
          
<class 'str'>
a="codegnan"
          
b="pfs"
          
a+b
          
'codegnanpfs'
a
          
'codegnan'
a*b
          
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'str'
a*10
          
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
b*9
          
'pfspfspfspfspfspfspfspfspfs'
'*'*20
          
'********************'
'python'*9
          
'pythonpythonpythonpythonpythonpythonpythonpythonpython'
'python '*9
          
'python python python python python python python python python '
names='naresh ajay akhil '
          
names
          
'naresh ajay akhil '
names[6]
          
' '
names
          
'naresh ajay akhil '
3
          
3
names
          
'naresh ajay akhil '
names[2]
          
'r'
names[11]
          
' '
names[12]
          
'a'
names[-1]
          
' '
names[-2]
          
'l'
names
          
'naresh ajay akhil '
#Slicing
          
#var[start:stop+1:step]
          
names[:7]
          
'naresh '
names[8:]
          
'jay akhil '
names[8:12]
          
'jay '
names:[14:]
          
SyntaxError: invalid syntax
names
          
'naresh ajay akhil '
names[-6]
          
'a'
names[-6:]
...           
'akhil '
>>> names[-12:-8]
...           
' aja'
>>> names[4::-1]
...           
'seran'
>>> names[::-1]
...           
' lihka yaja hseran'
>>> 'naresh' in names
...           
True
>>> 'virat' in names
...           
False
>>> 'naresh' not in names
...           
False
>>> 'akhil' in names
...           
True
>>> len(names)
...           
18
>>> names.upper()
...           
'NARESH AJAY AKHIL '
>>> names.lower()
...           
'naresh ajay akhil '
>>> max(names)
...           
'y'
>>> min(names)
...           
' '
>>> sorted(names)
...           
[' ', ' ', ' ', 'a', 'a', 'a', 'a', 'e', 'h', 'h', 'i', 'j', 'k', 'l', 'n', 'r', 's', 'y']
