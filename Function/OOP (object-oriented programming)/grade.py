class student:
    def __init__(self):
        self.name="Manu"
        self.regno="98745"
        print("STUDENT DETAILS")
        print("_________________")
        print("STUDENT NAME: ",self.name)
        print("REGISTER NUMBER: ",self.regno)

    def marks(self):
        print("Enter the marks")
        self.math=int(input())
        self.eng=int(input())
        self.cs=int(input())
        self.oops=int(input())
        self.dbms=int(input())
        self.avg=(self.math+self.eng+self.cs+self.oops+self.dbms)/5

    def cal(self,avg):
        if self.avg>=90:
            self.grade="A+"
        elif self.avg>=80:
            self.grade="A"
        elif self.avg>=70:
            self.grade="B+"
        elif self.avg>=60:
            self.grade="B"
        elif self.avg>=50:
            self.grade="C+"
        else:
            self.grade="Failed"

    def printgrade(self,grade):
        print("GRADE CARD")
        print("_______________")
        print("STUDENT NAME: ",self.name)
        print("REGISTER NUMBER ".self.regno)
        print("Grade",grade)
obj=student()
obj.marks()
obj.cal(obj.avg)
obj.printgrade(obj.grade)
