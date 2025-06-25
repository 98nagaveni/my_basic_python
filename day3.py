# UserFullName="undrasapu Nagaveni"    ''' these variable is called PASEAL CASE'''
# print(UserFullName)

# userFullName="yshuuu"                '''these variable is called CAMEL CASE'''
# print(friendsuserFullName)

# User_Full_Name="vaishaliii"           '''these variable is called SNAKE CASE'''
# print(User_Full_Name)

'''DAY=4 TOPIC:PYTHON LISTS'''
# friends=["hema,mouni,my_3,teja,ramya"] ''' BASIC  STRING LIST'''
# print(friends) 




# num=[2,19,14,15]      '''ONLY INTEGER LIST'''
# print(num)

# num.append(9.2000)    ''' THE LIST ALLOWS FLOAT VALUES'''
# print(num)

# num.append(True)      ''' THE LIST ALLOWS ALSO BOOLEAN VALUES '''
# print(num)
 
# friends.append("maha") ''' WE CAN ADD THE VALUE IN THE LIST BUT THE VALUE IS STORED END OF THE LIST'''
# print(friends)

# friends.insert(0,'sunny') '''WE CAN ADD THE PARTICULAR PLACE IN THE LIST BUT WE USE INDEXING WAY'''
# print(friends)

# friends.extend(["pushpa,reshma,swathi"])''' WE CAN ADD THE MULTIPLE VALLUES IN THE LIST'''
# print(friends)

# friends.sort(reverse=True) '''THE LIST ITEMS ARE REVERS ORDER'''
# print(friends)

# fruits=['apple','bannana','orange','grapes']
# print(fruits)

# fruits[2]='kiwi'  '''WE CAN ADD THE VALUE IN THE PARTICULAR PLACE WE CAN GIVEN THE INDEXING VALUE BUT THE LIST ITEMS ARE SEPERATED WITH COMMAS AND INVERTEDCOMMAS AND  '''
# print(fruits)        ''' AUTOMATICALLY  THE PREVIOUS VALUE WILL BE DELETED '''

# fruits[0:3]=['cherry','mango','apple'] ''' ABOVE THE SAME OPERATION BUT MULTIPLE VALUES ARE REPLACE'''
# print(fruits)

# fruits.remove('apple') '''REMOVE THE APPLE IN THE LIST'''
# print(fruits)

# fruits.pop(0)    '''ABOVE THE SAME OPERATION BUT DIFFERENT WAY'''
# print(fruits)


# fruits.sort()     ''' THE LIST ITEMS ARE ARRANGE THE ASCENDING ORDER '''
# print(fruits)

# friends.reverse()  '''THE LIST ITEMS ARE DESCENDING ORDER'''
# print(friends)
 
# del fruits[1]   '''THE PARTICULAR VALUE WILL BE DELETED'''
# print(fruits)

# fruits.clear() ''' THE TOTAL LIST ITEMS ARE CLEAR IT WILL BE REPRESENTED ONLY EMPTY LIST'''
# print(fruits)

# numbers=[23, 67, 1, 12, 166] '''  list also stored numbers'''
# print(numbers)

# numbers.sort()       ''' list items are ASCENDING ORDER'''
# print(numbers)

# numbers.sort(reverse=True) '''LIST ITEMS ARE DECENDINGB ORDER'''
# print(numbers)

# marks=[99, 80, 75, 30, 20]   
# print(marks)

# max(marks)      '''MaXIMUM VALUE PICK THE LIST'''
# print(max(marks))

# min(marks)     '''MINIMUM VALUE PICK THE LIST'''
# print(min(marks))

# '''outputs'''
# [23, 67, 1, 12, 166]
# [1, 12, 23, 67, 166]
# [166, 67, 23, 12, 1]
# [99, 80, 75, 30, 20]
# 99
# 20

'''DAY-5 TOPIC:TUPLE'''
# flowers=("rose","chamanthi","sunflower")
# print(flowers)
# flowersList=list(flowers)
# print(flowersList)
# flowersList.append(20)
# print(flowersList)
# flowersList[2]=True
# print(flowersList)
# flowers=tuple(flowersList)
# print(flowers)
'''OUTPUTS'''
# ('rose', 'chamanthi', 'sunflower')
# ['rose', 'chamanthi', 'sunflower']
# ['rose', 'chamanthi', 'sunflower', 20]
# ['rose', 'chamanthi', True, 20]
# ('rose', 'chamanthi', True, 20)


'''DAY-6 TOPIC:SET'''
# subjects={"maths","english","physics","telugu","chemistry",}''' basic set creation and set is an unorderd''' 
# print(subjects)

# print(len(subjects))  '''we can identify the set lenth use the len()'''

# animals={"dog","pig","dog"}'''the set duplicate values are not allowed'''
# print(animals)

# animals[0]="monkey" '''and indexing values are not applicable the set'''
# print(animals)

#myset={1,0.99,"apple",True}
#print(myset)
'''OUTPUTS'''
# {'chemistry', 'physics', 'maths', 'telugu', 'english'}
# 5
# {'pig', 'dog'}
# Traceback (most recent call last):
#   File "c:\Users\jagad\Desktop\pyhon\day3.py", line 117, in <module>
#     animals[0]="monkey"
#     ~~~~~~~^^^^^
#{0.99, 1, 'apple'}

'''DAY-7 TOPIC:DICTIONARY '''

# person={"firstname":"undrasapu","lastname":"nagaveni","mobile":00000}'''basic dictionary '''
# print(person)

# print(person["lastname"])'''ONLY WE CAN SEE THE ONE VALUE USE THESE METHOD'''

# person["age"]=19 '''WE CAN ADD THE ANOTHER VALUE IN DICTIONARY USE THESE WAY'''
# print(person)

# person["mobile"]="000000" '''THESE ALL NUBERS ARE PRINT GIVES THE ""S'''
# print(person)

# person.update({"mobile":"999999"}) '''ANOTHER WAY  WE CAN INSERT THE VALUE INTO DICTIONARY '''
# print(person)

# person.update({"date of birth":"22/07/2006"}) '''AND WE CAN UPDATE THE VALUE'''
# print(person)

# person={"firstname":"undrasapu","lastname":"nagaveni","mobile":00000}
# print(person)

# person2={"firstname":"undrasapu","lastname":"veera durga lakshmi","mobile":00000,"mobile":1234,"age":21}
# print(person2) '''duplicate values are not accesed in dictionary'''

# person2.pop("mobile") '''WE CAN DELETE THE VALUE IN DICTIONARY'''
# print(person2)

# person2.popitem() '''YOUR  DICTIONARY LAST ITEM PRINT USE THESE WAY'''
# print(person2)

# son={"firstname":"undrasapu","lastname":"veera","mobile":00000,"mobile":1878954,"age":21}
# print(son)

# son.clear()'''YOUR DICTIONARY VALUES ARE POP USE THESE WAY'''
# print(son)

# print(person.keys())   '''YOUR ALL DICTIONARY KEY ARE PRINT'''


# print(person.values()) '''YOUR ALL DICTIONARY  VALUES ARE  PRINT'''

# if "mobile" in person: ''' U CAN CHECK THE MOBILE NUMBER IN YOUR DICTIONARY USE THE IF STATEMENT'''
#     print("yes mobile number is placed in person") '''I AM CHECK MOBILE NUMBER IN PERSON'''
# else:
#     print("no mobile number is not placed in person")

# if "date of birth" in person:
#     print("yes date of birth  is placed in person")
# else:
#     print("no date of birth is not placed in person")

'''OUTPUTS'''

# {'firstname': 'undrasapu', 'lastname': 'nagaveni', 'mobile': 0}
# nagaveni
# {'firstname': 'undrasapu', 'lastname': 'nagaveni', 'mobile': 0, 'age': 19}
# {'firstname': 'undrasapu', 'lastname': 'nagaveni', 'mobile': '000000', 'age': 19}
# {'firstname': 'undrasapu', 'lastname': 'nagaveni', 'mobile': '999999', 'age': 19}
# {'firstname': 'undrasapu', 'lastname': 'nagaveni', 'mobile': '999999', 'age': 19, 'date of birth': '22/07/2006'}
# {'firstname': 'undrasapu', 'lastname': 'nagaveni', 'mobile': 0}
# {'firstname': 'undrasapu', 'lastname': 'veera durga lakshmi', 'mobile': 1234, 'age': 21}
# {'firstname': 'undrasapu', 'lastname': 'veera durga lakshmi', 'age': 21}
# {'firstname': 'undrasapu', 'lastname': 'veera durga lakshmi'}
# {'firstname': 'undrasapu', 'lastname': 'veera', 'mobile': 1878954, 'age': 21}
# {}
# dict_keys(['firstname', 'lastname', 'mobile'])
# dict_values(['undrasapu', 'nagaveni', 0])
# yes mobile number is placed in person
# no date of birth is not placed in person