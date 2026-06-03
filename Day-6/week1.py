name=input()
rollno=int(input())
s1=int(input())
s2=int(input())
s3=int(input())
total=s1+s2+s3
avg=total/3
print(f'Sudent Name:{name}')
print(f'Roll Number:{rollno}')
print(f'Total Marks:{total}')
print(f'Average Marks:{avg}')


s=input()
print('Total Characters:',len(s))
print('First Character:',s[0])
print('Last Character:',s[-1])
print('Uppercase:',s.upper())
print('Reversed String:',s[::-1])



a,b,c=list(map(int,input().split()))
print('Sum:',a+b+c)
print('Average:',(a+b+c)/3)
print('Product:',a*b*c)
