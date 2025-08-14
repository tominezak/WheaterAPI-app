# class variables = shared among aøll instances of the class - defined oustide of the constructor
# allow you to share data among all ojects created from that class

class Student:
    # Class variable
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student('Alice', 20)
student2 = Student('Bob', 22)

print(student1.name)  # Output: Alice
print(student2.name)  # Output: Bob
# print(student1.class_year)  # Output: 2024
print(Student.class_year)  # Output: 2024 - bedre praksis

print(Student.num_students)  # Output: 2