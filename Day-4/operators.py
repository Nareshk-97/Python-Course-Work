Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=20
a+b
30
a-b
-10
a*b
200
a/b
0.5
a//b
0
a%b
10
a**b
100000000000000000000
9/2
4.5
9//2
4
7%3
1
7/3
2.3333333333333335
7//3
2
17%3
2
a=20
b=10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
y=5
y
5
y=y+5
y
10
y=y+10
y
20
y +=10
y
30
y -=10
y
20
y *=4
y
80
y //=10
y
8
y %=2
y
0
y +=10
y
10
y /=2
y
5.0
y
5.0
y **=10
y
9765625.0
a=20
a
20
b=10
b
10
a%10==0
True
a%20==0 and b%20==0 and a>b
False
False
False
a%20==0 or b%20==0 or a>b
True
not a>b
False
#str,list,tuple,dict,set
a='python programming'
a
'python programming'
'y' in a
True
z in a
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    z in a
NameError: name 'z' is not defined
'z' in a
False
'z' not in a
True
l=['java','python','mysql','c++','c']
'mysql' in l
True
'c' not in a
True
t=('lap','mou')
t
('lap', 'mou')
'lap' in t
True
'char' in t
False
t={1,2,3,4,5}
t
{1, 2, 3, 4, 5}
1 in t
True
9 in t
False
50 not in t
True
d={'egg':8,'oil':100}
'oil' in d
True
8 in d
False
'egg' in d
True
'chilli' in d
False
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
n==m
True
l==m
True
l is m
False
n is m
True
id(l)
2132411575936
id(m)
2132411816640
id(n)
2132411816640
l is not m
True
l is not n
True
8 & 14
8
8 & 7
0
8 | 7
15
10^11
1
~12
-13
8>>2
2
15>>1
7
16<<1
32
4<<2
16
a=12
b=12.34
c='python'
print(a,b,c)
12 12.34 python
print('a=',a,'b=',b,'c=',c)
a= 12 b= 12.34 c= python
print('a=',a,'b=',b,'c=',c,sep='\n'))
SyntaxError: unmatched ')'
print('a=',a,'b=',b,'c=',c,sep='\n)
      
SyntaxError: unterminated string literal (detected at line 1)
print('a=',a,'b=',b,'c=',c,sep='\n')
      
a=
12
b=
12.34
c=
python
>>> python
...       
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> print('a=',a,'b=',b,'c=',c,sep='')
...       
a=12b=12.34c=python
>>> print('a=',a,'b=',b,'c=',c,sep='',end='@@@@')
...       
a=12b=12.34c=python@@@@
>>> print(f'a={a},b={b} c={c}')
...       
a=12,b=12.34 c=python
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
...       
a=12 b=12.34 c=python
>>> print(('a={} b={} c={}'.format(a,b,c))
... 
... 
... 
... print(('a={} b={} c={}'.format(a,b,c))
...       print(('a={} b={} c={}'.format(a,b,c))
... print('a={} b={} c={}'.format(a,b,c))
...             
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('a= {2} b={0} c={1}'.format(a,b,c))
...             
a= python b=12 c=12.34
>>> print(('a= {} b={} c={}'.format(a,b,c))
... print('a= {2} b={0} c={1}'.format(a,b,c))
...       
SyntaxError: '(' was never closed
>>> print('a= {2} b={0} c={1}'.format(a,b,c))
...       
a= python b=12 c=12.34
>>> print('a= {} b={} c={}'.format(a,b,c))
...       
a= 12 b=12.34 c=python
