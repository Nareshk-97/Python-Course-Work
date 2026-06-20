#List Comp.


res=[]
for i in range(1,11):
    res.append(i)
print(res)




#
res3=[]
for i in range(3,31,3):
    res3.append(i)
print(res3)


#
res4=[i for i in range(2,51,2)]
print(res4)


#
res=[i for i in range(5,51,10)]
print(res)




#String
a="Python Programming"
l=[]
for i in a:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)

#Comp. 
l1=[i for i in a if i in 'aeiouAEIOU']
print(l1)





l=[val for var in seq]
l=[val for var in seq if condition]
l=[val if condition else val for var in seq]



#
a=[1,2,3,4,5,6,7,8,9,12,5,87,56,45,98]
l=[]
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)
print(l)
#comp
l1=[i if i%2==0 else 0 for i in a]
print(l1)


#Comp
l=[int(input(f"Enter the number - {i+1}: ")) for i in range(10)]
print(l)



#
l=[]
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)

#Comp
l1=[j for i in range(3) for j in range(1,4)]
print(l1)



#Comp
l1=[[j for j in range(1,4)] for i in range(3)]
print(l1)



#
s=set()
for i in range(1,11):
    s.add(i)
print(s)

#Comp
s1={i for i in range(1,11)}
print(s1)





##Dict Comp
d={}
for i in range(1,11):
    d[i]=i*i
print(d)


#comp
res={i:i*i for i in range(1,20)}
print(res)



#Comp
res={input("Enter the name: "):int(input("Enter the Mark: "))for i in range(5)}
print(res)




##Generator
def display():
    l=['1...50','51...100','101...150','151...200']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]
scroll=display()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
        



