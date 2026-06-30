

#Read Operations
file=open('sample.txt','r')

print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()



#Exception
try:
    file=open('samples.txt','r')
except FileNotFoundError:
    print("File is not there")
    
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())

    file.close()




#without file close
with open('sample.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())





#append file
with open('sample.txt','a') as file:
    file.write('praneeth\nshiva\nsrikanth')




#Write mode-->Overridden
with open('sample.txt','w') as file:
    file.write('praneeth\nshiva\nsrikanth')




#read and write 
with open('sample.txt','w+') as file:
    file.write('praneeth\nshiva\nsrikanth')
    file.seek(0)
    print(file.read())




#
with open('demo.txt','w+') as file:
    file.write('praneeth\nshiva\nsrikanth')
    file.seek(0)
    print(file.read())
    



#os Module
import os
os.mkdir('Sample')



#remove file
import os
os.rmdir('Sample')






#Regular Expression
import re
pattern='[a-z]'
text='naresh'
res=re.match(pattern,text)
print(res.group() if res else "No Match Found")






#Search
import re
pattern='[0-9]'
text='Python version 3.15'
res=re.search(pattern,text)
print(res.group() if res else "No Match Found")





#findall
import re
pattern='[a-z]'
text='Python version 3.15'
res=re.findall(pattern,text)
print(res)





#finditer
import re
pattern='[a-z]'
text='Python version 3.15'

res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())




#fullmatch
import re
pattern='[a-z]{9}'
text='abcdefghi'
res=re.fullmatch(pattern,text)
print(res.group() if res else "No Match Found")





#split
import re
pattern=r'[,a+yn]'
text='java,python,c++'
res=re.split(pattern,text)
print(res)




#sub--.replacing
import re
pattern=r'[0-9]{2}'
text='java: 34,python: 98,c++: 55'
res=re.sub(pattern,'**',text)
print(res)




