Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='   hello      world     '
s
'   hello      world     '
s.strip()
'hello      world'
s.lstrip()
'hello      world     '
s.rstrip()
'   hello      world'
s='string.py'
s
'string.py'
s.startswith('str')
True
s.startswith('gfg')
False
s.endswith('py')
True
s.endswith('js')
False
'hwjefgg'.isalpha()
True
'deuiehd@12333'.isalpha()
False
'3456789'.isalpha()
False
'123456789'.isalnum()
True
'fghuytrfghuihgkh'.isalnum()
True
'fgdhdygvfdhjsdh1234567'.isalnum()
True
'naresh'.islower()
True
'sdfghjkl12345!@#$%^'.islower()
True
'SDFGHJ!!!!!!@#$%12345'.isupper()
True
' '.isspace()
True
'hello         '.isspace()
False
'Py Prg Lan'.istitle()
True
'Py prg'.istitle()
False
'py_prg'.isidentifier()
True
'py@123'.isidentifier()
False
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2,3,4]
m=[5,6,7,8,9]
l+m
[1, 2, 3, 4, 5, 6, 7, 8, 9]
l*m
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    l*m
TypeError: can't multiply sequence by non-int of type 'list'
l*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l=[10,20,30,40,90]
l[4]
90
l[2]
30
l=[-3]
l
[-3]
l[-3]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    l[-3]
IndexError: list index out of range
l
[-3]
l=[10,20,30,40,50,50]
l
[10, 20, 30, 40, 50, 50]
l[-3]
40
l[-1]
50
l[1]
20
l[1:4]
[20, 30, 40]
l[::-1]
[50, 50, 40, 30, 20, 10]
l[-1:-4:-1]
[50, 50, 40]
l[-3::-1]
[40, 30, 20, 10]
l
[10, 20, 30, 40, 50, 50]
20 in l
True
40 in l
True
100 in l
False
90 not in l
True
70 in l
False
l
[10, 20, 30, 40, 50, 50]
id
<built-in function id>









9
l
[10, 20, 30, 40, 50, 50]
id(l)
2245544318016
l[l]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    l[l]
TypeError: list indices must be integers or slices, not list
l[1]
20
l
[10, 20, 30, 40, 50, 50]
l[1]=70
l
[10, 70, 30, 40, 50, 50]
id(l)
2245544318016
l[4]=90
l
[10, 70, 30, 40, 90, 50]
l
[10, 70, 30, 40, 90, 50]
l.append(120)
l
[10, 70, 30, 40, 90, 50, 120]
l.append(300)
l
[10, 70, 30, 40, 90, 50, 120, 300]
l.insert(1,20)
l
[10, 20, 70, 30, 40, 90, 50, 120, 300]
l.insert(6,69)
l
[10, 20, 70, 30, 40, 90, 69, 50, 120, 300]
l.extend([80,90,110])
l
[10, 20, 70, 30, 40, 90, 69, 50, 120, 300, 80, 90, 110]
l
[10, 20, 70, 30, 40, 90, 69, 50, 120, 300, 80, 90, 110]
l.pop()
110
l
[10, 20, 70, 30, 40, 90, 69, 50, 120, 300, 80, 90]
l.pop()
90
l
[10, 20, 70, 30, 40, 90, 69, 50, 120, 300, 80]
l.pop(3)
30
l
[10, 20, 70, 40, 90, 69, 50, 120, 300, 80]
l.pop(9)
80
l
[10, 20, 70, 40, 90, 69, 50, 120, 300]
l.pop(2)
70
l
[10, 20, 40, 90, 69, 50, 120, 300]
l.remove
<built-in method remove of list object at 0x0000020AD4DF1440>
l
[10, 20, 40, 90, 69, 50, 120, 300]
l.remove(50)
l
[10, 20, 40, 90, 69, 120, 300]
l.remove(300)
l
[10, 20, 40, 90, 69, 120]
del l[1]
l
[10, 40, 90, 69, 120]
del l[1]
l
[10, 90, 69, 120]
del l[1]
l
[10, 69, 120]
l.clear()
l
[]
l=[200,30,45,456,68,456,900,469]
l
[200, 30, 45, 456, 68, 456, 900, 469]
sorted(l)
[30, 45, 68, 200, 456, 456, 469, 900]
l.sort()
l
[30, 45, 68, 200, 456, 456, 469, 900]
min{1}
SyntaxError: invalid syntax
min(l)
30
max(l)
900
l
[30, 45, 68, 200, 456, 456, 469, 900]
l.reverse()
L
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    L
NameError: name 'L' is not defined. Did you mean: 'l'?
L
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    L
NameError: name 'L' is not defined. Did you mean: 'l'?
>>> 
>>> l
[900, 469, 456, 456, 200, 68, 45, 30]
>>> l.reverse()
>>> l
[30, 45, 68, 200, 456, 456, 469, 900]
>>> l.sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    l.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> l.sorted(l,reverse=True)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    l.sorted(l,reverse=True)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> sorted(l,reverse=True)
[900, 469, 456, 456, 200, 68, 45, 30]
>>> l
[30, 45, 68, 200, 456, 456, 469, 900]
>>> l.index
<built-in method index of list object at 0x0000020AD4DD70C0>
>>> l.index(200)
3
>>> l.index(469)
6
>>> l.count(900)
1
>>> l.append(30)
>>> l
[30, 45, 68, 200, 456, 456, 469, 900, 30]
>>> l.count(30)
2
>>> l
[30, 45, 68, 200, 456, 456, 469, 900, 30]
>>> any([1,2,3,4,0,0,0,0,0,0])
True
>>> all([1,2,3,4,5,0,0,0,0])
False
