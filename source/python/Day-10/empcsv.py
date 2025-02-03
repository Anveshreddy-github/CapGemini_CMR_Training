import csv
def get_employee_details():
    emp=[]
    name=input("enter employee name:")
    emp_id=input("enter employee id:")
    emp.append({'name':name ,'id':emp_id})
    return emp

# def insert_into_csv(emp,filename='employee.csv'):
#     with open(filename, mode='a',newline='') as file:
#         writer=csv.DictWriter(file,fieldnames=['name','id'])
#         writer.writeheader()
#         writer.writerows(emp)
def insert_into_csv(emp, filename='employee_details.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'id'])
        writer.writeheader()
        writer.writerows(emp)

def main():
    emps=get_employee_details()
    insert_into_csv(emps)
    print("employee details have been inserted into csv files")
main()