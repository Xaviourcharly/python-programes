class student:
    def open(self):
        print("school open")
class teacher:
    def close(self):
        print("closed")
class school(student,teacher):
    def start(self):
        print("hi studens")

obj=school()
obj.close()
obj.start()
