#exercise 1
width = 17 
height = 12.0 
delimiter = '.'
def value_x(var1, cons1):
	c = var1/cons1
	d = type(c)
	return c,d
print("ans of exercise1.1 ",value_x(width, 2))  
print('ans of exercise1.2 ',value_x(width, 2.0))
print('ans of exercise1.3 ',value_x(height, 3))
c=1+2*5
print('ans of exercise1.4 ',c, type(c))
e = (delimiter * 5)
print("ans of excercise1.5 ",e, type(e))

#exercise2
def fahtoc(fahren): #function to convert fahrenheit to celcius
	ftoc = ((float(fahren)-32)*5)/9
	return ftoc 
print(fahtoc(49)) #calling the function as well as printing the
					#returned value 

#exercise3
def mintosec(sec):  #function to convert seconds into minute
	mtos = sec/60    #and seconds
	s = sec%60
	return mtos,s
print(mintosec(3845)) #calling and printing the value

#exercise4
elem_list =['a', 'abc', 'def', 'kukur', 'biralo']
print('length is ',len(elem_list))  #printing the length
print('first element',elem_list[0],'fourth element', elem_list[3])
#printing the first and fourth element

#exercise5
an_elem_list = ['tomato', 'potato', 'pumpkin', 'cake']
print(an_elem_list)
an_elem_list.pop() #pop method
print(an_elem_list)
an_elem_list.insert(0,'aalu') #inserting method
print(an_elem_list)
an_elem_list.remove('tomato') #removing methog
print(an_elem_list)
