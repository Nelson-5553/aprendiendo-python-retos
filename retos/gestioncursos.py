class Student:

    def __init__ (self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
 
    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)  # Aquí se agrega el estudiante al curso automáticamente
        print(f"Curso de {course.title} ha sido agregado")
    
    def show_courses(self):
        print ("estas incrito en el curso de")
        for curso in self.courses:
            print(curso.title)
        
class Course:
    def __init__ (self, title, code):
        self.title = title
        self.code = code
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print(f"Curso de {student.name} ha sido agregado")

    def show_student(self):
        print(f"Los estudiantes incritos al curso de {self.title}")
        for estudiante in self.students:
            print(estudiante.name)


    
class School:
    def __init__ (self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Curso de {student.name} ha sido agregado")
    
    def add_course(self, course):
        self.courses.append(course)
        print(f"Curso de {course.title} ha sido agregado")

estudiante1 = Student("Nelson", 101)
estudiante2 = Student("Naty", 102)
estudiante3 = Student("Gledis", 103)

curso1 = Course("Python", 201)
curso2 = Course("PHP", 202)
curso3 = Course("JavaScript", 203)


estudiante1.enroll(curso1)
estudiante1.show_courses()

curso1.show_student()





        
