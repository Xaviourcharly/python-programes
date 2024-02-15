class Student():
    def attendance(self,n_s):
        d={}
        print("enter the attendance roll number wise")
        for k in range(n_s):
            x=int(input())
            d[k]=x
            self.s=list(d)

class Teacher(Student):
    def teach_det(self):
        self.name=input("enter the name of the teacher:")
        self.code=input("enter the code of the teacher:")
        self.sal=int(input("enter the basic salary of the teacher:"))
        self.dept=input("enter the number of the students:")
        obj.attendance(self.n_s)
        obj.print_details(obj.s)

def print_details(self,s):
            print(i)
            print("___________")
            print("Name: \t",self.name)
            print("Empcode:\t",self.code)
            print("Department:\t",self.dept)
            print("Basic salary \t",self.sal)
            self.da=self.sal*0.1
            print("DA: \t,",self.da)
            self.hra=self.sal*.13
            print("HRA: \t",self.hra)
            self.pf=self.sal*.06
            print("PF \t",self.pf)
            self.net=self.sal+self.pf+self.hra+self.da
            print("Net salary: \t",self.net)
            print("list of present students",)
            for x in range(self.n_s):
                if self.s[x]==1:
                    print(x)
            print("list of absent students")
            for y in range(self.n_s):
                if self.s[y]==0:
                    print(y)
obj=Teacher()
n_t=int(input("enter the number of Teachers:"))
for i in range(1,n_t+1):
    obj.teach_det()
    #for j in rnge(1,n_t+1

