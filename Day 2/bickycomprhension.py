# LIST COMPREHENSION:
#even list:
list  =[i for i in range(10) if i%2==0]
print(list)

#  for square print:
numbers =[1,2,3,4,5]
sqr=[x** 2 for x  in numbers]
print(sqr)

#DICTIONARY COMPREHENSION:
sqr_dict={num: num*num for num in range(1,11)}
print(sqr_dict)

    
