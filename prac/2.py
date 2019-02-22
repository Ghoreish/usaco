import time
class student:
    def __init__(self,name,birth):
        self.name=name
        self.birth=int(birth)
    @property
    def age(self):
        x=int(time.strftime("%Y"))-self.birth
        return x
    def show(self):
        print(self.name,"\t",self.age)
ali=student("Ali Ghoreishi",1999)
ali.show()