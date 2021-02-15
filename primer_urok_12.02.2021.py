# def squares():
#     print('Hello world!')
# squares()
#
# def squares(x):
#     print('Hello world!')
# squares("jfkj")
#
# def squares(x):
#     x=x**2
#     print(x)
# squares(5)

x=10
def squares(number):
    print(number)
    number=20
    print(number)
squares(x)
print(x)

def squares(number): #funkziju mi pishem cherez def
    square=number**2
    return square   #return prinimajet znachenije kakoi-to funkzii
squares (5)
print(squares(5))
print(type(squares(5)))

def double(number):
    double=number*2
    return double
print(double(4))

def squares(x):
    y=x**2
    return y

def multiplier(number, multiplier):
    result=number*multiplier
    return result
multiplier(4,6)

for number in range (1,101):
    print(squares(number))

def area (a,b):
    area=a*b
    return area

def perimeter (a,b):
    perimeter=2*(a+b)
    return perimeter
# def print_message(name, age, profession):
#     return print('Hi my name is '+name+'. I am '+age+' years old. I work as a', profession, '.')
# user_name, user_age, user_profession=input('Enter name, age and profession divided by space: ').split(' ')
# print(input('Enter name, age and profession divided by space: ').split(', '))
# print_message(user_name, user_age, user_profession)
#
# side_a=5
# side_b=10
# print(area(side_a,side_b))
#
# employee=['John', 'Smith', '32', '5000', 'Tallinn']
# def print_employee_message(employee_data):
#     name=employee_data[0]
#     last=employee_data[1]
#     age=employee_data[2]
#     salary=employee_data[3]
#     town=employee_data[4]
#     return 'Hello ' + name+ ' ' +last+ '. You are '+age+' years old. Your salary is '+ salary+ ' EUR. You are from ' + town
# print(print_employee_message(employee))



def id_check(id_code, chk_list):
    counter=0
    result=0
    for num in chk_list:
        result +=int(id_code[counter])*num
        counter+=1
    return result % 11

id_code=list(input('Please enter your id: '))
chk1=[1,2,3,4,5,6,7,8,9,1]
chk2=[3,4,5,6,7,8,9,1,2,3]
if id_check(id_code, chk1)==10:
    result=id_check(id_code, chk2)
    if result==int(id_code[10]):
        print('ID code is valid')
    else:
        print('ID code is invalid')
elif id_check(id_code, chk1)==int(id_code[10]):
    print('ID code is valid')
else:
    print('Your ID code is invalid')