class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"My name is {self.name}")

class Employee(person):
    def __init__(self, name,id):
        super().__init__(name)
        self.id=id

    def display(self):
        print(f"Name is : {self.name} and employee_id is {self.id}")

class manager(Employee):
    def __init__(self, name, id):
        super().__init__(name, id) 
    def approve_leave(self,days):
        self.days=days
        print(f"Manager has approved leave of {self.name} withn id {self.id} for {self.days}")


def main():
    p=person("Ram")
    p.display()
    e=Employee("ram",44)
    p.display()
    m=manager("ram",44)
    m.approve_leave(4)
main()
