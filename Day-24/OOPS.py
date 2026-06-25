
'''

class Flipkart:
    discount=10
    products=['laptop','phone','mouse','charger']

    @classmethod
    def showproducts(cls):
        print(cls.products)

    def login(self,username,password):
        self.username=username
        self.password=password
        print(f'welcom to the flipkart {self.username}')

    @staticmethod
    def banner():
        print("10% discount is going on flipkart,shop now!")
naresh=Flipkart()
naresh.login('naresh','naresh@123')
naresh.banner()
naresh.showproducts()
Flipkart.showproducts()

'''


#Encapsulation
#constructor
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self.followers=[]

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password=newpassword

naresh=Instagram('naresh','naresh@123')

print("Aefore username:",naresh.username)
naresh.username='akhil'
print("After username:",naresh.username)

print("Before password:",naresh.getpassword())
naresh.setpassword('akhil@123')
print("After password:",naresh.getpassword())
