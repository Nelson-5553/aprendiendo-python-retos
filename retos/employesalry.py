class Employee:
    def __init__ (self, name, position, salary: int):
        self.name = name
        self.position = position
        self.salary = salary

    def show_info(self):
        print(f"Nombre: {self.name}\n position: {self.position}\n Salario: {self.salary}\n")

    def  apply_raise(self):
        self.salary *= 1.10
        print("El nuevo salario es: ", self.salary)

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"El empleado {employee.name} ha sido agregado")
        
    
    def show_all_employees(self):
        for empleado in self.employees:
            empleado.show_info()

    def total_payroll(self):
        total = sum(emp.salary for emp in self.employees)
        print("Nómina total:", total)

empleado1 = Employee("Nelson", "Desarrollador", 1200)
empleado2 = Employee("Naty", "Desarrolladora", 1300)
empleado3 = Employee("Gledis", "Diseñadora", 1400)
# empleado1.show_info()
empleado1.apply_raise()

company = Company()

company.add_employee(empleado1)
company.add_employee(empleado2)
company.add_employee(empleado3)
company.show_all_employees()

company.total_payroll()