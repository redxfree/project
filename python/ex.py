if __name__ == '__main__':
     
    nums = [1, 5, 2, 1, 4, 5, 1]
 
    dup = [x for i, x in enumerate(nums) if x in nums[:i]]
    print(dup)  
    
    
    
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

res = []
for i in test_list:
	if i not in res:
		res.append(i)

# printing list after removal
print ("The list after removing duplicates : " + str(res))


