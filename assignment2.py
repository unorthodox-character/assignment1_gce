#exercise 1
list_one = [1,43,54,5,6,12,2]
sum = 0
for i in range(len(list_one)):
	sum += list_one[i]
print(sum)

#exercise 2
list_a = [1,1,3,5,7,9,9]
list_b = [2,1,6,9,2,1,3,5]
list_c = []
list_d = []
for i in range(len(list_a)):
	for j in range(len(list_b)):
		if list_a[i] == list_b[j]:
			list_c.append(list_a[i])
			

for i in list_c:
	if i not in list_d:
		list_d.append(i) 
print(list_d)


#exercise 3
list_three = [1,7,3,9,4]
for i in range(len(list_three)):
 	print('the items inthe list are:', list_three[i])
for i in range(len(list_three)):
	print('the square of each no. in the list is:',list_three[i]*list_three[i])	

# exercise 4
print('enter a strign')
value = input()
list_string = list(value)
count = 0
for i in range(len(list_string)):
    count += 1
print('u entered a string: ', value, 'and the length of your string is:', count)

#exercise 5 
print('enter a strign')
value = input()
print('the upper case is:',value.upper())
print('the lower case is:',value.lower())