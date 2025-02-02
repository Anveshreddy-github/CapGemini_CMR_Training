class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    
    def student_details(self):
        return f" My name is  {self.name} and Rollno is {self.rollno}"
    
def main():
    name=input("enter your name :")
    rollno=input("enter rollno:")
    p=student(name,rollno)
    print(p.student_details())
main()