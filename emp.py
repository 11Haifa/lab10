class EmpSystem:
    def __init__(self):
        self.employees = []

    def create(self, name, age, emp_id, department):
        employee = {
            'name': name,
            'age': age,
            'id': emp_id,
            'department': department
        }
        self.employees.append(employee)
        print("Employee created successfully.")

    def retrieveEmp(self, emp_id):
        for employee in self.employees:
            if employee['id'] == emp_id:
                return employee
        return None

    def deleteEmp(self, emp_id):
        for employee in self.employees:
            if employee['id'] == emp_id:
                self.employees.remove(employee)
                print("Employee deleted successfully.")
                return
        print("Employee not found.")

# Example
e = EmpSystem()

e.create("Haifa Hussein", 22, 1, "IT")
e.create("John Doe", 30, 2, "HR")

employee_info = e.retrieveEmp(1)
if employee_info:
    print("Employee Found:")
    print(employee_info)
else:
    print("Employee not found.")

# e.deleteEmp(2)
