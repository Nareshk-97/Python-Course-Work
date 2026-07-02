
#\
import re

pattern=r'h.t\b'
text='hot hit het hrt hat hate hood heart hjt h$t'

res=re.findall(pattern,text)
print(res)




#^ starts with
import re

pattern=r'^h'
text='hot hit het hrt hat hate hood heart hjt h$t'

res=re.findall(pattern,text)
print(res)





#$ checking for ends
import re

pattern=r't$'
text='hot hit het hrt hat hate hood heart hjt h$t'
res=re.findall(pattern,text)
print(res)





#* 1 or many
import re

pattern=r'to*'
text='too to t toooooo tooooooooo'

res=re.findall(pattern,text)
print(res)





#? atleast 1 or 0
import re

pattern=r'to?\b'
text='too to t toooooo tooooooooo'

res=re.findall(pattern,text)
print(res)






#{}
import re

pattern=r'[a-z]{5}'
text='gfd f ergde ugrdf hotde ghy tfrdtrs'

res=re.findall(pattern,text)
print(res)






#() exactly match pattern
import re

pattern=r'(python)'
text='pyth  pythn python pythh'

res=re.findall(pattern,text)
print(res)







#Form validation

#Name validate
import re

pattern=r'^[a-zA-Z] {2,15} ([a-zA-Z] {2,15})+$'
text=input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")




#Email validate
import re

pattern=r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
text=input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")






#Phone number valid
import re

pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
text=input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")





#Password validate
import re

pattern=r'^(?=.*[A-Z]) (?=.*[a-z]) (?=.*\d) (?=.*[@$!%*?&]) [A-Za-z\d@$!%*?&] {8,} $'
text=input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")




#Username validate
import re

pattern=r'^[a-zA-Z0-9]{5,15}$'
text=input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")







