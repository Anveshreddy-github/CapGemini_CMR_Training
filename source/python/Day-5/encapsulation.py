class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def set_salary(self,salary):
        self.__salary=salary
    
    def get_salary(self):
        return self.__salary
    
    def cal_allowance(self,percentage):
        return self.__salary * (percentage/100)
    
    def cal_deduction(self,amount):
        return amount

emp=Employee("alica",50000)
allowance=emp.cal_allowance(8)
deduction=emp.cal_deduction(5000)

print("Allowance:",allowance)
print("After Deduction:",deduction)
print("The new salary as per allowance:",emp.get_salary()+allowance)
new_salary=emp.get_salary()+allowance
after_deduction=new_salary-deduction
print("the total salary after dedution is : ",after_deduction)

# emp=Employee("alica",50000)
# print("Salary before update",emp.get_salary())
# emp.set_salary(100000)
# print("salary after update",emp.get_salary())
# emp_new_salary=input("enter new salary:")
# emp.set_salary(emp_new_salary)
# print("the new salary as per input:",emp.get_salary())    
