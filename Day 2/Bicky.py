#NESTED LIST
print("FOR NESTED LIST:")
li=[10,15,23,17,[20,35,30,80,70,49]]
print(li)
print (len(li))
print (len(li[4]))
print (li[4][-1])
print (li[4][:])
print (li[4][1:3])
print (li[4][ : : 2])
li.append(100)
print(li)

#NESTED TUPLE
print("FOR NESTED TUPLE:")
tup=(8,10,4.6,(45,"mouse","bicky",28),(2.0,"hello",46))
print(tup)
print(tup[3])
print(tup [3][2])
print(tup[:4])

#NESTED DICTIONARY
print("FOR NESTED DICTIONARY:")
fmember = {
                  1: {'name': 'bicky', 'age': '24', 'sex': 'male'},
                  2: {'name': 'rocky', 'age': '6', 'sex': 'male'},
                  3: {'name': 'lucky', 'age': '29', 'sex': 'male'},
                  4: {'name': 'liza', 'age': '18', 'sex': 'female'},
                  5: {'name': 'bini', 'age': '24', 'sex': 'female'},
                  }
    
print(fmember)
print(fmember[2]['name'])
print(fmember[2]['age'])
print(fmember[2]['sex'])
fmember[6]= {'name': 'lusi', 'age': '21' , 'sex': 'female'}
print(fmember)
fmember[1]['name']='bunty'
print(fmember[1])
fmember[3]['dob']=1996
print(fmember[3])
    

      
      
