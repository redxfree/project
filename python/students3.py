marks = [23, 56, 81, 79, 58, 37, 36, 70, 32, 65]
ages = [18, 21, 17, 30, 14, 8, 20, 21, 25, 16]


def calc_total(a):
    total = 0
    for i in a:
        total = total + i
    return total

def calc_average(a):
    total = calc_total(a)
    average = total/len(a)
    return average



def filter_list_marks(age, mm ):
    filter_list = []
    for i in mm:
        if i>=age:
            filter_list.append(i)
    return filter_list


def teen (marks, ages):
    total = 0
    cnt = 0
    for i in ages:
        if i>=13 and i<=19:
            total = total + marks[cnt]
        cnt+= 1
    return total



def high_low(marks):
    min = 100
    max = 0
    for i in marks:
        if i<=min:
            min = i
        if i>=max:
            max = i
    total = max - min
    return total
    
            
def percentile(marks):
    percentile_is = 0
    for i in marks:
        if i<56:
            percentile_is+= 1
        total = percentile_is/len(marks)*100
    return total            
     
    

 
            
            


# 1. Print average of all marks
avg = calc_average(marks)
print(avg)

avg_age = calc_average(ages)
print(avg_age)


# 2. Print how many students got first class(greater than 60)
new_list = filter_list_marks(60 , marks)
print(len(new_list))

# 3. What is the total of marks of teenagers teen_
marks_teen = teen(marks, ages)
print(marks_teen)

# 4. What is differnce of marks between student getting highest mark and lowest mark
differnce = high_low(marks)
print(differnce)

# 5. What is the percentile of student getting 56 marks
student  = percentile(marks)
print(student)

    
        
   

    

