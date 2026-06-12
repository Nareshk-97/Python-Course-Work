#While Loop

'''
int
while condition:
    upd
    #stat


i=1
while i<11:
    print(i)
    i+=1

    

i=2
while i<21:
    print(i)
    i+=2


i=10
while i>0:
    print(i)
    i-=11
    


i=5
while i<51:
    print(i)
    i+=5



l=[1,20,3,4,5,7,9]
i=0
while i<len(l):
    print(l[i])
    i+=1



l='Python Programming'
i=0
while i<len(l):
    print(l[i])
    i+=1


    

l=(1,20,3,4,5,7,9)
i=0
while i<len(l):
    print(l[i])
    i+=1




l=[1,0,0,2,3,4,0,0,0,2,0,0,1,0,3,50,2,0,64,23,0,0,0,0,0,12,3,34]
while 0 in l:
    l.remove(0)
print(l)





moves=30
while moves>1:
    status=input("[W] in or [C]ontinus: ").upper()
    if status=='W':
        print("You won the game")
        break
    moves-=1
    print(f'{moves} moves are left')
else:
    print("Game Over!")


'''
