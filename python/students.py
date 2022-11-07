marks = [23, 56, 81, 79, 58, 37, 36, 70, 32, 65]
ages = [18, 21, 17, 30, 14, 8, 20, 21, 25, 16]


# 1. Print average of all marks
# 2. Print how many students got first class(greater than 60)
# 3. What is the total of marks of teenagers
# 4. What is differnce of marks between student getting highest mark and lowest mark
# 5. What is the percentile of student getting 56 marks


# 1. Print average of all marks

total = 0
for i in marks:
    total = total + i
q = total/len(marks)
print('Average is\n ' + str(q))    
    
    

# 2. Print how many students got first class(greater than 60)

cnt = 0
for i in marks:
    if i>=60:
        cnt +=1
print('These many students\n'+ str(cnt))
      

# 3. What is the total of marks of teenagers

total = 0
cnt = 0
for i in ages:
    if i>=13 and i<=19:
        total = total + marks[cnt]
    cnt+=1
print("the total marks of teenagers is \n"+ str(total))


# 4. What is differnce of marks between student getting highest mark and lowest mark

min = 100
max = 0
for y in marks:
    if y<=min:
        min = y
    if y>=max:
        max = y
diferrence = max-min
print("difference is "+ str(diferrence))
    
    
# 5. What is the percentile of student getting 56 marks

number_less =0
    

for i in marks:
    if i<56:
        number_less +=1
pecrcentile = number_less/len(marks)*100
print("percentile is "+ str(pecrcentile))    


    