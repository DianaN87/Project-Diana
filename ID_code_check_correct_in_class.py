id_code=input('Please enter your ID code: ')
#1234567891
#3456789123
# control_number=(1*int(id_code[0])+2*int(id_code[1])+3*int(id_code[2])+4*int(id_code[3])\
#                +5*int(id_code[4])+6*int(id_code[5])+7*int(id_code[6])+8*int(id_code[7])+9*int(id_code[8]+1*int(id_code[9])))%11
# if control_number==int(id_code[-1]):
#     print('OK')
# elif control_number==10:
#     control_number2=3*int(id_code[0])+4*int(id_code[1])+5*int(id_code[2])+6*int(id_code[3])\
#                     +7*int(id_code[4])+8*int(id_code[5])+9*int(id_code[6])+1*int(id_code[7])+2*int(id_code[8])+3*int(id_code[9])


chk1=[1,2,3,4,5,6,7,8,9,1]
chk2=[3,4,5,6,7,8,9,1,2,3]
id_code_list=list(id_code)
print(id_code_list)
counter=0
result=0
for num in chk1:
    result=result+chk1[counter]*int(id_code_list[counter])
    counter +=1
check_num=result % 11
if check_num==int(id_code[-1]):
    print ('ID code is valid')
elif check_num==10:
    counter=0
    result=0
    for num in chk2:
        result=result+chk2[counter]*int(id_code_list[counter])
        counter +=1
    check_num=result % 11
    if check_num== int(id_code[-1]):
        print('Code is correct1') # why is not correct???
    elif check_num>=10:
        if id_code[-1] !=0:
            print('Please check Your ID code')
        else:
            print('ID code is correct xxx')
    else:
        print('Code is not valid yyy')
else:
    print('Code is not valid!!!!')

