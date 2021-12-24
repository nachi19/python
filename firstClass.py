class Employee:
    cname= "GMIT"
    def __init__(self,eno,ename,sal):
        self.eno=eno  #instance variable
        self.ename=ename
        self.sal=sal

    def info(self): # instance methods
        print("Eno ", self.eno)
        print("ename ",self.ename)
        print("sal" , self.sal)

    @classmethod
    def clasMethods(cls):
        print(cls.cname)
    @staticmethod
    def addMarks():
        marks=20
        print(marks)
    def print(self):
        print(self.__dict__)

    def delete(self): #deleting instance variable inside class
        del self.ename

e1=Employee(123,"Nachi",1000)
e2=Employee(e1.eno,e1.ename,e1.sal)
e1.info()
e2.info()
e1.age=30 # adding instance variable outside class
e1.addMarks()
e1.clasMethods()
e2.clasMethods()
e1.print()

del e1.age # deleting instance variable

#del e1.age
e1.delete()

e1.print()