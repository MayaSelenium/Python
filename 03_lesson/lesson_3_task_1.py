class User:
    def __init__(self, first_name, last_name):
        self.myname=first_name
        self.mylast_name=last_name
    def MN(self):
        print("Имя",self.myname )
    def MLN(self):
        print("Фамилия", self.mylast_name)
    def MNMLN(self):
        print("Имя и фамилия",self.myname,self.mylast_name)
