class employee:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def display(self):
        print(f"the records of employe are name :{self.name} and age is : {self.age}")
# class main():
#     emp1=employee("abc",19)
#     emp2=employee("qwe",76)
#     emp3=employee("sgr",66)
#     emp4=employee("fsa",22)
#     list_emp=[emp1,emp2,emp3,emp4]
#     for i in list_emp:
#         i.display()
# main()

def get_input():
    name=input("enter name:")
    age=input("enter age:")
    return name,age

class main():
    n=int(input("enter no of records:"))
    list_emp=[]
    for i in range(n):
        name,age=get_input()
        list_emp.append(employee(name,age))
    for i in list_emp:
        i.display()
main()