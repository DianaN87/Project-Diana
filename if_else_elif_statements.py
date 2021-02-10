id_code= input ('Please enter Your national id: ')

if len(id_code)==11:
    print('Your ID code is', id_code)
elif len(id_code)>11:
    print('Code You entered is longer than 11 digits')
else:
    print('Code You entered is shorter than 11 digits')

if len(id_code)==11:
    print('Your ID code is', id_code)
else:
    print('WRONG')

some_string="Hello world. It is a beautiful day"
if "beautiful" in some_string:
    print('beautiful is in some_string variable')
else:
    print('beautiful is not in some_string variable')
if len(some_string)>10:
    print("Some string is greater than 10 characters")
elif len(some_string)>20:
    print("Some string is also greater than 20 characters")
if len(some_string[0>5])>10:
    print("Some string is greater than 10 characters")
elif len(some_string)>20: # pokazivajet potomu chto if nevernoje
    print("Some string is also greater than 20 characters")

some_number=100
if some_number >10 and some_number>200:
    print("Some string is greater than 10 characters")
else:
    print("ERROR")

if "world" in some_string:
    print ("YES")
else:
    print ("NO")

if ("world" in some_string)==True:
    print("YES")
else:
    print("NO")

some_string= 'Hello world'
print(some_string.replace(some_string[4:8], ''))
print(some_string.replace('world', 'people'))
print (some_string)

some_string= some_string.replace('world', 'people')
print(some_string)

new_string= '''When hjfehkfje'''
print(new_string)
print(new_string.replace(',',''))



