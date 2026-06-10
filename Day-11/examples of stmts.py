
data={
    'subbu':{'status':True,'python':98,'mysql':95,'flask':94},
    'naresh':{'status':True,'python':78,'mysql':85,'flask':84},
    'dinesh':{'status':False,'python':None,'mysql':None,'flask':None},
    'nagendra':{'status':True,'python':68,'mysql':65,'flask':54},
    'rishi':{'status':True,'python':33,'mysql':25,'flask':34},
    }
name=input("Enter the name: ")
if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=total/3
        if avg > 90:
            print(f"Congrations {name}, you got first class!!!")
        elif avg > 70:
            print(f"Good {name}, keep it the next time!!")
        elif avg>35:
            print(f"Better {name}, work hard next time!")
        else:
            print(f" {name}, you have failed in the exam.Bring your paresnts.")
    else:
        print(f"{name} did't write the exam.Bring your parents")
else:
    print(f"{name}'s data ia not found")





        
    
budget=int(input("Enter the budget: "))
if budget > 50000:
    print("you can go for the trip")
elif budget > 30000:
    print("you can go for the pub")
elif budget > 10000:
    print("you can go for the shopping")
elif budget > 5000:
    print("you can go for the cafe")
elif budget > 2000:
    print("you can go for the movie")
elif budget > 500:
    print("you can recharge your phone")
else:
    print("Take Rest")
