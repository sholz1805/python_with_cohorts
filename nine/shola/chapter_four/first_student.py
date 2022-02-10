# write a python class named student with two attributes student_name, marks. modify the attribute values of the
# said class and print the original and modified values of thr said attributes

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def get(self):
        return self.student_name, self.marks

    # def __str__(self):
    #     return self.student_name + " " + str(self.marks)


student = Student("Shola", 55)
print(student.student_name, student.marks)

student.marks = 60
student.student_name = "Shola Azeez"

print(student.student_name, student.marks)


# Write a python class named Student with two attributes student_id, student_name. Add a new attribute student_class
# and display the entire attribute and their values of the said class. Now remove the student_name attribute and
# display the entire attributes with values.
class StudentB:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = "C9"


studentB = StudentB("001", "Shola Azeez")

print(studentB.student_id, studentB.student_name, studentB.student_class)
print(studentB.__dict__)
studentB.__setattr__("student_name", "Ola")
print(studentB.__dict__)

studentB.__dict__.update({"class": "C9"})
print(studentB.__dict__)
