Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Tuple
t=(1,1,1,1,1,1)
t
(1, 1, 1, 1, 1, 1)
t=(10,20,30,40)
h=(50,60,70)
t+h
(10, 20, 30, 40, 50, 60, 70)
t*4
(10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40)
t
(10, 20, 30, 40)
t[2]
30
t[3]
40
t[-2]
30
t[-1]
40
t
(10, 20, 30, 40)
t(:3)
SyntaxError: invalid syntax
t[:3]
(10, 20, 30)
t
(10, 20, 30, 40)
t[3:]
(40,)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40)
t[::2]
(10, 30)
t[-1:-4:-1]
(40, 30, 20)
t
(10, 20, 30, 40)


10 in t
True
90 in t
False
100 not in t
True
t
(10, 20, 30, 40)
len(t)
4
sorted(t)
[10, 20, 30, 40]
min[t]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    min[t]
TypeError: 'builtin_function_or_method' object is not subscriptable
min(t)
10
max(t)
40
t.count(20)
1
t.count(40)
1
t.index(10)
0
a=(1,2,3)
a
(1, 2, 3)
x,y,z=a
x
1
y
2
z
3
t=(1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
t[3]
[4, 5, 6, 10]
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
#Sets
s={1,2,3,4}
s
{1, 2, 3, 4}
s=set()
s={1,1,1,1,1,1,1}
s
{1}
s={123,643,7644,7,975,90,6,908,3}
s
{3, 643, 6, 7, 908, 975, 90, 123, 7644}
s
{3, 643, 6, 7, 908, 975, 90, 123, 7644}
s=set()
s
set()
s.add(1)
s
{1}
s
{1}
s={123,643,7644,7,975,90,6,908,3}
s
{3, 643, 6, 7, 908, 975, 90, 123, 7644}
s.add(47,48)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s.add(47,48)
TypeError: set.add() takes exactly one argument (2 given)
s
{3, 643, 6, 7, 908, 975, 90, 123, 7644}
s=set()
s
SyntaxError: multiple statements found while compiling a single statement
s=set()
s
set()
s.add(1)
s
{1}
s.add(54.43)
s
{1, 54.43}
s.add("dfghj")
s
{1, 54.43, 'dfghj'}
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: unhashable type: 'list'
s
{1, 54.43, 'dfghj'}
1 in s
True
2 in s
False
43 not in s
True
a={1,2,3,5,6,8,9,10}
b={6,7,8,9}
a | b
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{8, 9, 6}
a & b
{8, 9, 6}
a - b
{1, 2, 3, 5, 10}
a ^ b
{1, 2, 3, 5, 7, 10}
a
{1, 2, 3, 5, 6, 8, 9, 10}
#{1}{2}{3}{4}{5{6}
a<={1}
False
a>={1}
True
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a
{1, 2, 3, 5, 6, 8, 9, 10}
a.add(69)
a
{1, 2, 3, 5, 6, 69, 8, 9, 10}
a.add(19)
a
{1, 2, 3, 5, 6, 69, 8, 9, 10, 19}
a.update({11,12,13})
a
{1, 2, 3, 5, 6, 69, 8, 9, 10, 11, 12, 13, 19}
a.pop()
1
a.pop()
2
a.remove(13)
s
{1, 54.43, 'dfghj'}
a
{3, 5, 6, 69, 8, 9, 10, 11, 12, 19}
a.remove(13)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.remove(13)
KeyError: 13
a.remove(13)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.remove(13)
KeyError: 13
a.remove(11)
a
{3, 5, 6, 69, 8, 9, 10, 12, 19}
>>> s.discard(6)
>>> a.discard(6)
>>> a
{3, 5, 69, 8, 9, 10, 12, 19}
>>> a.discard(3)
>>> a
{5, 69, 8, 9, 10, 12, 19}
>>> a.clear()
>>> a={1,4,23,57,235}
>>> a
{1, 4, 23, 57, 235}
>>> b={1,2,4,34}
>>> b
{1, 2, 4, 34}
>>> a.intersection_update(b)
>>> a
{1, 4}
>>> b
{1, 2, 4, 34}
>>> c=b
>>> c.add(12)
>>> c
{1, 2, 34, 4, 12}
>>> d=c.copy()
>>> d.add(10)
>>> d
{1, 2, 34, 4, 10, 12}
>>> c
{1, 2, 34, 4, 12}
>>> len(c)
5
>>> min(c)
1
>>> max(c)
34
>>> sorted(c)
[1, 2, 4, 12, 34]
>>> sum(c)
53
