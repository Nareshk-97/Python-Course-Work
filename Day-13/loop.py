'''

seq:str,list,tuple,set,dict
for i in freq:
    #stmts

# 1.

pin=1234
for i in range(5):
    e_pin=int(input("Enter the Pin: "))
    if e_pin==pin:
        print("Unlock the phone")
        break
    else:
        print("incorrect pin")
else:
    print("Try again, after 60 seconds")


# 2.

l=[2,5,7,9,4,78,23,12,10]
a=int(input("Enter the number: "))
for i in range(len(l)):
    if l[i]==a:
        print(f'{a} is found at index -{i}')
        break
else:
    print(f'{a} is not found')




password=input("Enter the Password: ")
if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')
    if len(s)==4:
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")
    
      
'''
