"""
 Student
  name
  phone
  email
  password
  isCollegeTraining
  collegeName
  rollNum

class student:
    pass
student = s1
s1.name = "John"
s1.phone = "+91 99999 77777"
s1.email = "john@gmail.com"
s1.password = "pass123"
s1.iscollegeTraining = True
s1.collegeName = " abc"
s1.rollNum = 123

student = s2
s2.fullName = "John"
s2.phone = "+91 99999 77777"
s2.email = "john@gmail.com"
s2.password = "pass123"
s2.iscollegeTraining = True
s2.collegeName = " abc"
s2.roll = 123
"""
#challenge: No standardistaion
#Solution:  constructors



class Student:

    # self is a referencevariable which will hold hashcode of current object
    #__init__ is known as constructor
    #constructor is property of class
    def __init__(self, name,phoneNumber, email, password, isCollegeTraining, collegeName, rollNum):
        print(">>self is:",self)
        self.fullname = name
        self.phone = phoneNumber
        self.email = email
        self.password = password
        self.isCollegeTraining = isCollegeTraining
        self.collegeName = collegeName
        self.rollNum = rollNum

    def showStudentDetails(self):
        print("details of:",self.fullname)

s1 = Student("John", "+91 99999 77777", "John@example.com", "pass123", True, "ABC", 22)
print("s1 is : ", s1)

s2 = Student("rahul", "+91 99333 77777", "Rahul@example.com", "pass123", True, "ABC", 28)
print("s2 is : ",s2)
s1.age= 76
s1.vehicle = "ferrari"

s1.fullname
#print(s1.__dict__)
#print(s2.__dict__)


# follow github sir