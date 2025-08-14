# class methods = methods that are bound to the class and not the instance. 
# They can be called on the class itself, and they take the class as the first argument (usually named `cls`).

class Student:

    count = 0
    total_gpa = 0  # Class variable to keep track of total GPA

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # hver gang et objekt opprettes, økes telleren med 1
        Student.total_gpa += gpa

    # instans method
    def get_info(self):
        return f'Student Name: {self.name}, GPA: {self.gpa}'
    
    # class method
    @classmethod
    def get_student_count(cls):
        return f'Total # of students: {cls.count}'  # Return the total number of Student instances created
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        return f'Average GPA: {cls.total_gpa / cls.count:.2f}'  # Return the average GPA of all students

    
student1 = Student('Alice', 3.8)
student2 = Student('Bob', 3.5)
student3 = Student('Charlie', 3.9)

print(Student.get_student_count())  
print(Student.get_average_gpa())  