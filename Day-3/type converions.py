Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
bool(0)
False
s='python'
a='1234'
b='1234.5678'
int(a)
1234
float(a)
1234.0
float(b)
1234.5678
list(a)
['1', '2', '3', '4']
list(b)
['1', '2', '3', '4', '.', '5', '6', '7', '8']
list(s)
['p', 'y', 't', 'h', 'o', 'n']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
set(s)
{'h', 'y', 't', 'o', 'n', 'p'}
{'h', 'y', 't', 'o', 'n', 'p'}
{'p', 'h', 'n', 'y', 't', 'o'}
tuple(b)
('1', '2', '3', '4', '.', '5', '6', '7', '8')
>>> bool(b)
True
>>> bool(0.0)
False
>>> c=2+3j
>>> str(c)
'(2+3j)'
>>> float(a)
1234.0
>>> float(b)
1234.5678
>>> list(a)
['1', '2', '3', '4']
>>> list(b)
['1', '2', '3', '4', '.', '5', '6', '7', '8']
>>> list(s)
['p', 'y', 't', 'h', 'o', 'n']
>>> tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
>>> set(s)
{'h', 'y', 't', 'o', 'n', 'p'}
>>> bool(s)
True
>>> complex(a)
(1234+0j)
>>> complex(b)
(1234.5678+0j)
>>> l
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> l=[1,2,3,4,5,6,7]
>>> l
[1, 2, 3, 4, 5, 6, 7]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
