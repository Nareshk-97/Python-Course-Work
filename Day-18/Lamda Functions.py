
'''
def display(s,ind):
    if ind==len(s):
        return
    print(s[:ind+1])
    display(s,ind+1)
display("abcdrfghijklmn",0)





#
def display(s,ind,l):
    if ind==len(s)-l+1:
        return
    print(s[ind:ind+l])
    display(s,ind+1,l)
display("Python",0,2)






#
def display(l,ind):
    if ind==len(l):
        return 0
    return l[ind]+display(l,ind+1)
l=[1,2,3,4,5,6,78]
print(display(l,0))
    






#
def display(s,i):
    if i==len(s):
        return 0
    if s[i] in 'aeiouAEIOU':
        return 1+display(s,i+1)
    else:
        return display(s,i+1)
s='Python Programming'
print(display(s,0))





