from datetime import datetime,  timedelta
from typing import Dict

b =1.2
print(type(b))

b="eee"
print(type(b))

c = datetime.now()
print(type(c))
print(c)

c= c+timedelta(minutes=-2)
print(c)

print(c.date())
#==================================================

class Student():
    def __init__(self):
        self.name="Sarah"
        self.age=22
        self.course = "BE"

s= Student()
s.name = "N"
s.age = "21"
s.course = "BTech"

t= Student()
t.name = "O"
t.age = "27"
t.course = "BCOM"

students = [s,t]

for stud in students:
    print(stud.name)
    
#=====================================================

#Create dictionary of Students . 
# FIrst input how many students should be there
# Use input to get name, age and course of all students.
# Print all the names of the students
#Find total age of all the students. 
# Create a list out of this Dictionary which will count of different course
dict = {}


w = input('how many students should be there\n')

students = []
for i in range(int(w)):
    student = Student()
    student.name = input('Enter Student name: ')
    student.age = int(input('Enter Student age: '))
    student.course = input('Enter Student course: ')
    
    students.append(student)

class Student():
    def __init__ (self):
        self
        
        
# x =Student()        
# x.name = "jagu"
# x.age = 21
# x.course = "bsc"

       
# d = Student()
# d.name = "roy"
# d.age = 22
# d.course = "bcom"


# e = Student()
# e.name = "shem"
# e.age = 22
# e.course = "bcom"

# students = [x,d,e]

# for i in students:
#     print(i.name, i.age , i.course)
    
    
for s in students:
    print(s.name)
    
    
total = 0
for a in students:
    total = total + a.age
print(total)
average = total/len(students)

# Create a list out of this Dictionary which will count of different course

count = 0
courses ={}

for f in students:
    if f.course in courses.keys():
        # Add one to count of course
        current_count = courses[f.course]
        current_count+=1
        courses[f.course] = current_count
    else:
        #Add a new key 
        courses[f.course] = 1
    
print(courses)

