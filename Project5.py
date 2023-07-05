class Student:

  def __init__(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender

  def info(self):
    print(f"Name:{self.name} | Age:{self.age} | Gender:{self.gender}")
    

ram = Student("Ram", 18, "Male")
ram.info()

male_students = ["SM1","SM2","SM3","SM4"]
female_students = ["SF1","SF2","SF3","SF4"]
student_list = [("SM1",19,"Male"),("SF1",20,"Female")]

students = []

for name, age, gender in student_list:
  s = Student(name, age, gender) #instance
  students.append(s)
  #s.info()

for student_name in male_students:
  students.append(Student(student_name,18,"Male"))

for student_name in female_students:
  students.append(Student(student_name,18,"Female"))

for student in students:
  student.info()