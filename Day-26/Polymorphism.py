
'''

#Polymorphism
class Hotstar:
    def __init__(self,name):
        self.name=name
        print(f'Hi {self.name}, Welcome to the hotstar')
    def login(self):
        print("you can login")
    def dashboard(self):
        print("you can see the dashboard items")
    def search(self):
        print("you can search")
    def lang(self):
        print("you select the languages")
    def playcontrollers(self):
        print("you can pause and play the video")
    def ads(self):
        print("ads will run")
    def movies(self):
        print("you can limited access for moves")
    def sports(self):
        print("limited time you can watch sports")
    def quality(self):
        print("limited quality")


class PremiumHotstar(Hotstar):
    def __init__(self,name):
        self.name=name
        print(f'Hi {self.name}, Welcome to the Premium Hotstar')
    def ads(self):
        print("ads won't run")
    def movies(self):
        print("you can unlimited access for moves")
    def sports(self):
        print("you can watch sports")
    def quality(self):
        print("High quality")



class GoldPremiumHotstar(Hotstar):
    def __init__(self,name):
        self.name=name
        print(f'Hi {self.name}, Welcome to the GoldPremium Hotstar')
    def ads(self):
        print("ads won't run")
    def movies(self):
        print("you can unlimited access for moves")
    def sports(self):
        print("you can watch sports")
    def quality(self):
        print(" very High quality")
    def downloads(self):
        print("videos download unlimited")   


naresh=Hotstar('naresh')
naresh.login()
naresh.dashboard()
naresh.search()
naresh.lang()
naresh.playcontrollers()
naresh.ads()
naresh.movies()
naresh.sports()
naresh.quality()
    
akhil=PremiumHotstar('akhil')
akhil.login()
akhil.dashboard()
akhil.search()
akhil.lang()
akhil.playcontrollers()
akhil.ads()
akhil.movies()
akhil.sports()
akhil.quality()
    
ajay=GoldPremiumHotstar('ajay')




'''

class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n*other.n
    def __eq__(self,other):
        return self.n==other.n
    def __lt__(self,other):
        return self.n<other.n
    def __gt__(self,other):
        return self.n>other.n
    def __truediv__(self,other):
        return self.n/other.n
    def __str__(self):
        return str(self.n)

n1=Number(10)
n2=Number(20)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1/n2)
print(n1,n2)

