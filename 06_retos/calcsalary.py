
def show_salary(empleados, sueldo):

    for i in empleados:
        if i["salary"] >= sueldo :
            print(f"los empleados con un sueldo mayor o igual a {sueldo} son {i["name"]}") 

employees = [
    {"name": "Juan", "age": 28, "salary": 3500},
    {"name": "María", "age": 32, "salary": 4200},
    {"name": "Carlos", "age": 25, "salary": 3100},
    {"name": "Ana", "age": 40, "salary": 5000},
    {"name": "Luis", "age": 30, "salary": 3900},
]

show_salary(employees, 4000)