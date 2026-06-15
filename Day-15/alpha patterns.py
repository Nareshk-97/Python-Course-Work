 

'''

n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()




n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print('*',end=' ')
    else:
        for j in range(n-i):
            print('*',end=' ')
    print()






n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    if i<=m:
        print('  '*(m-i),end=' ')
        print('* '*(i+1),end=' ')
    else:
        print('  '*(i-m),end=' ')
        print('* '*(n-i),end=' ')
    print()






n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i),end=' ')
        print('* '*(i+1),end=' ')
    else:
        print(' '*(i-m),end=' ')
        print('* '*(n-i),end=' ')
    print()







n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    if i<=m:
        print('  '*(m-i)+'* '*(i+1),end=' ')
    else:
        print('  '*(i-m)+'* '*(n-i),end=' ')
    print()







n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()





# sq lle'l and horiz'l
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
      







# square cross
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or j==i or i+j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()




# A 
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



# B
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



# C

n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()




#D

n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()




#E

n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or i == n//2 or i == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



#F

n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or i == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()





#H

n = int(input("Enter the size: "))
m = n // 2
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == m:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



'''



n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == m:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if i == 0 or (j == m and i != n-1) or (i == n-1 and j <= m):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()





n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if j == 0 or i + j == m or i - j == m:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

