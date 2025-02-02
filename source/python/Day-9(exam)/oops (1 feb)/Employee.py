class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department

    def get_name(self):
        print(f"hello {self.name}")
    def get_id(self):
        print(f"My id is : {self.id}")
    def get_dept(self):
        print(f"I work in the department {self.department}")

def main():
    name=input("enter your name:")
    id=input("enter ur id:")
    dept=input("enter ur department:")
    p=Employee(name,id,dept)
    p.get_name()
    p.get_id()
    p.get_dept()
main()