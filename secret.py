#2017年木犀后台机试题答案
class User():
    def __init__(self):
        self.ucountry = None

    def cmethod(cls):
        print("Nationality {}".format(cls.ucountry))
    def hello(self):
        print("Hello,I'm User", end="")
    def smethod(self):
        print("Just a normal user")

class ChineseUser(User):
    def __init__(self):
        self.ucountry = 'China'
    def hello(self):
        print("I'm ChineseUser", end="")

class RussianUser(User):
    def __init__(self):
        self.ucountry = 'RussianUser'
    def hello(self):
        print("I'm RussianUser", end="")

class ChineseRussianUser(RussianUser, ChineseUser):
    def __init__(self):
        self.ucountry = "China && Russia"
    def hello(self):
        super().hello()
        print(" So, I'm ChineseRussianUser")

    
#Test:
u = ChineseRussianUser()
u.hello()
u.smethod()
u.cmethod()
