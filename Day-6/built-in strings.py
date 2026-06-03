Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="Python Programming"
len(s)
18
sorted(s)
[' ', 'P', 'P', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord(s)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ord(s)
TypeError: ord() expected a character, but string of length 18 found
ord('a')
97
ord('b')
98
ord('A')
65
ord('s')
115
ord(' ')
32
chr(98)
'b'
chr(30)
'\x1e'
chr(37)
'%'
s
'Python Programming'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'pYTHON pROGRAMMING'
"SCHWYFOWTDBAJWHV".casefold()
'schwyfowtdbajwhv'
s.center(38,'*')
'**********Python Programming**********'
s.center(28,'*')
'*****Python Programming*****'
s.center(28,'-')
'-----Python Programming-----'
s.ljust(28,'-')
'Python Programming----------'
s.rjust(28,'-')
'----------Python Programming'
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'
'123'.zfill(3)
'123'
'123'.zfill(2)
'123'
s
'Python Programming'
s.find('0')
-1
s.find('o')
4
s.find('g')
10
s.rfind('o')
9
s.find('z')
-1
s.index('o')
4
s.rindex('o')
9
s
'Python Programming'
\
s.count('y')
1
s.count('m')
2
s.count('g')
2
s
'Python Programming'
s.replace('python','java')
'Python Programming'
s.replace('python','java')
'Python Programming'
s.replace('Python','Java')
'Java Programming'
s.maketrans('Python','123456')
{80: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('Python','123456'))
'123456 1r5grammi6g'
##splitting & Joining Methods
s='java','python','javascript','c','c++')
SyntaxError: unmatched ')'
s='java','python','javascript','c','c++'
s.split(',')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s.split(',')
AttributeError: 'tuple' object has no attribute 'split'
s.split(',')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s.split(',')
AttributeError: 'tuple' object has no attribute 'split'
s='java,python,javascript,c,c++'
>>> s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
>>> s.split(',',2)
['java', 'python', 'javascript,c,c++']
>>> s.rsplit(',',2)
['java,python,javascript', 'c', 'c++']
>>> g='sdfgh'
>>> 
>>> g='''hgktfgjhgyiuh'''
>>> g='''gdsagdhwe
... gerah;
... dfsgD
... DSGAWDGTEG'''
>>> g
'gdsagdhwe\ngerah;\ndfsgD\nDSGAWDGTEG'
>>> s.splitlines()
['java,python,javascript,c,c++']
>>> g.splitlines()
['gdsagdhwe', 'gerah;', 'dfsgD', 'DSGAWDGTEG']
>>> l=['java','python','javascript','c','c++']
>>> ''.join(l)
'javapythonjavascriptcc++'
>>> '-'.join(l)
'java-python-javascript-c-c++'
>>> '@'.join(l)
'java@python@javascript@c@c++'
>>> ' '.join(l)
'java python javascript c c++'
>>> ','.join(l)
'java,python,javascript,c,c++'
>>> s
'java,python,javascript,c,c++'
>>> s.partition(',')
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
>>> text = "Hello नमस्ते你好 café 🙂"
>>> text.encode()
b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'
>>> b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'.decode()
'Hello नमस्ते你好 café 🙂'
