def simple():  
 for i in range(100):  
    if(i%2==0):  
         yield i  

for i in simple():  
    print(i)
