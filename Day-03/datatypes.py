Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
t=999.99
type(t)
<class 'float'>
c=6+9j
type(c)
<class 'complex'>
s='python'
type(s)
<class 'str'>
s="ahdjk"
type(s)
<class 'str'>
s='''dcnj'''
type(s)
<class 'str'>
l=[1,2,3,4]
id(l)
2742951565888
l.append(20)
l.append(30)
l
[1, 2, 3, 4, 20, 30]
>>> l=['post.png','reel.mp4']
>>> l
['post.png', 'reel.mp4']
>>> l=[]
>>> l=list90
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l=list90
NameError: name 'list90' is not defined. Did you mean: 'list'?
>>> l=list()
>>> type(l)
<class 'list'>
>>> 
>>> t=()
>>> t=(1,2,3,4,5,6)
>>> t
(1, 2, 3, 4, 5, 6)
>>> type(t)
<class 'tuple'>
>>> s={1,2,3,4,5}
>>> type(s)
<class 'set'>
>>> s=set()
>>> s={434,6556,785,}
>>> a
10
>>> s
{785, 434, 6556}
>>> d={'name':'naresh','age':21,'course':'PFS'}
>>> d
{'name': 'naresh', 'age': 21, 'course': 'PFS'}
>>> type(d)
<class 'dict'>
>>> status=True
>>> status=False
>>> type(status)
<class 'bool'>
>>> a=None
>>> type(a)
<class 'NoneType'>
