from typing import OrderedDict


a = [4, 8, 5, 11, 87, 34, 23, 90, 24, 51, 68]

# 1. Print all the odd numbers
# 2. Print the sum of all even numbers
# 3. Print average of all numbers
# 4. Find if sum of odd numbers is greater or lesser than sum of even numbers


# 1. Print all the odd numbers
for i in a:
    if i%2==1:
        print(i)



# 2. Print the sum of all even numbers
total = 0
for i in a:
    if i%2==0:
        total = total + i 
print('total is ' + str(total))    


# 3. Print average of all numbers

total = 0
for i in a:
    total = total + i 
  
avg = total/len(a)

print('Aver+age is ' + str(avg))    





# 4. Find if sum of odd numbers is greater or lesser than sum of even numbers
odd_total =0
even_total =0
for i in a:
    if i%2==1:
        odd_total = odd_total + i
           

for i in a:
    if i%2==0:
        even_total = even_total + i 


if odd_total > even_total:
    print('Odd is greater- ' + str(odd_total))
else:
    print('Even is greater- ' + str(even_total))   

