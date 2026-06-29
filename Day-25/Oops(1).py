
'''

#Property
class Instagram:
    def __init__(self):
        self._post=[]

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

naresh=Instagram()

print(naresh.accesspost)
naresh.accesspost='class and object'
print(naresh.accesspost)

        



#Inheritance types
#1.single 
class whatsapp1:
    def message(self):
        print("you can send messages to peopele")

class whatsapp2(whatsapp1):
    def calls(self):
        print("You can do video/audio calls")

dinesh=whatsapp1()
print("v1- Dinesh")
dinesh.message()

naresh=whatsapp2()
print("v2- Naresh")
naresh.message()
naresh.calls()





#2.Multiple
class whatsapp1:
    def message(self):
        print("you can send messages to peopele")

class whatsapp2:
    def calls(self):
        print("You can do video/audio calls")

class whatsapp3:
    def media(self):
        print("You can share your photos/videos")

class whatsapp4(whatsapp1,whatsapp2,whatsapp3):
    def status(self):
        print("You can share status-[24 hours]")

naresh=whatsapp4()
print("v4- Naresh")
naresh.message()
naresh.calls()
naresh.media()
naresh.status()





#Multilevel

class whatsapp1:
    def message(self):
        print("you can send messages to peopele")

class whatsapp2(whatsapp1):
    def calls(self):
        print("You can do video/audio calls")

class whatsapp3(whatsapp2):
    def media(self):
        print("You can share your photos/videos")

class whatsapp4(whatsapp3):
    def status(self):
        print("You can share status-[24 hours]")

akhil=whatsapp3()
print("v3- Akhil")
akhil.message()
akhil.calls()
akhil.media()

naresh=whatsapp4()
print("v4- Naresh")
naresh.message()
naresh.calls()
naresh.media()
naresh.status()






#Hierarchy

class whatsappv1:
    def message(self):
        print("you can send messages to peopele")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("you can send messages with emojis to people")

class whatsappv3(whatsappv1):
    def stickers(self):
        print("you can send messages with stickers to people")

naresh=whatsappv3()
print("v4")
naresh.stickers()
naresh.message()
naresh.emojis()





#Hybrid
class whatsappv1:
    def message(self):
        print("you can send messages to peopele")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("you can send messages with emojis to people")

class whatsappv3(whatsappv1):
    def stickers(self):
        print("you can send messages with stickers to people")

class whatsappv4(whatsappv3,whatsappv2):
    def gif(self):
        print("you can send messages with gif to people")

naresh=whatsappv4()
print("v4")
naresh.stickers()
naresh.message()
naresh.emojis()
naresh.gif()






#super()

class whatsappv1:
    def status(self):
        print("you can upload images/videos")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("you can react and reply")

class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("you can like and reshare")

naresh=whatsappv3()
naresh.status()






#class
class whatsappv1:
    def status(self):
        print("you can upload images/videos")

class whatsappv2:
    def status(self):
        print("you can react and reply")

class whatsappv3(whatsappv2,whatsappv1):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("you can like and reshare")

naresh=whatsappv3()
naresh.status()




'''



