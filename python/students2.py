marks = [77, 34, 11, 40, 62, 75, 88, 40]
ages = [18, 21, 17, 30, 14, 8, 20, 21]

#1 average of ages
total = 0
for i in ages:
    total = total + i
avg = total/len(ages)
print("avergae is "+ str(avg))    

#2 total marks of people students who are more than 18 years old


total = 0
for i in marks:
    total = total + i
print("total marks is"+ str(total))    

#3 What is the total of marks of teenagers
cnt = 0
total = 0
for i in ages:
    if i>=13 and i<=19:
        total = total + marks[cnt]
    cnt+= 1
print("teenagers total marks is"+ str(cnt))       


# 4. What is differnce of marks between student getting highest mark and lowest mark

min = 100
max = 0
for i in marks:
    if i<=min:
        min=i
    if i>=max:
        max =i   
    total = max - min
print("differrence is "+ str(total))        

# 5. What is the percentile of student getting 56 marks

marks_less = 0

for i in marks:
    if i<56:
        marks_less +=1
        total = marks_less/len(marks)*100
print("percentile is\n"+ str(total))                