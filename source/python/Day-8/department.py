from abc import ABC,abstractmethod
from typing import List
class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass
    def get_salary(self) -> float:
        pass

class manager(Employee):
    def __init__(self,name:str,salary:float):
        self.name=name
        self.salary=salary

    def work(self)->str:
        return f"{self.name} is a manager of the team"
    def get_salary(self)->float:
        return self.salary
    
class developer(Employee):
    def __init__(self,name:str,salary:float):
        self.name=name
        self.salary=salary
    def work(self)->str:
        return f"{self.name} is working on the project"
    def get_salary(self)->float:
        return self.salary

class intern(Employee):
    def __init__(self,name:str,salary:float):
        self.name=name
        self.salary=salary
    def work(self)->str:
        return f"{self.name} is learing"
    def get_salary(self)->float:
        return self.salary
    
class department:
    def __init__(self,name:str):
        self.name=name
        self.employee:List[Employee]=[]

    def hire(self, employee: Employee) -> None:
        self.employee.append(employee)
        print(f"{employee.name} has been hired.")

    def fire(self, employee: Employee) -> None:
        self.employee.remove(employee)
        print(f"{employee.name} has been fired.")

    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employee)

    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:")
        for employee in self.employee:
            print(f"- {employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")

class Security(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is Securing the assets."

    def get_salary(self) -> float:
        return self.salary
    
m=manager("alica",80000)
d=developer("bob",70000)
i=intern("charile",40000)
s=Security("barli",20000)

p=department("sales")
p.hire(m)
p.hire(d)
p.hire(i)
p.hire(s)
p.show_employee_details()

total_salary=p.get_total_salary()
print(f"Total salary expenses for {p.name} is : {total_salary} ")