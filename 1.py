class Student:
    education = "Step"
    group = "C2924"
    subject = "OOP Python"

    def __init__(self, name="Inna", age="10", height="130"):
        self.name = name
        self.age = age
        self.height = height
        print("__INIT__")
        # print(id(self))

st1 = Student("Oleg", 15, 155)
st2 = Student("Anna", 16, 160)
st3 = Student("Petro", 18, 170)
st4 = Student("Ruslan", 21, 190)
st5 = Student()

print(Student.education)
print(st1.age)
print(st2.age)
print(st3.age)
print(st4.age)
print(st5.age)
print(st1.name)
print(st2.name)
print(st3.name)
print(st4.name)
print(st5.name)

# print(id(st1))

# st1 = Student()
# print(st1.group)
# print(st1.education)
# st2 = Student()
# print(st2.group)
# st2.group = "C2925"
# print(st2.group)
