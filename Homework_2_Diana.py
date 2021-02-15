user_id = input('Please enter your national id: ')
first_module=('1234567891')
second_module=('3456789123')
print(user_id[0])
result_sum=int(user_id[0])*int(first_module[0])+int(user_id[1])*int(first_module[1])+int(user_id[2])*int(first_module[2])+int(user_id[3])*int(first_module[3])+int(user_id[4])*int(first_module[4])+int(user_id[5])*int(first_module[5])+int(user_id[6])*int(first_module[6])+int(user_id[7])*int(first_module[7])+int(user_id[8])*int(first_module[8])+int(user_id[9])*int(first_module[9])
print(result_sum)
result_sum2=int(user_id[0])*int(second_module[0])+int(user_id[1])*int(second_module[1])+int(user_id[2])*int(second_module[2])+int(user_id[3])*int(second_module[3])+int(user_id[4])*int(second_module[4])+int(user_id[5])*int(second_module[5])+int(user_id[6])*int(second_module[6])+int(user_id[7])*int(second_module[7])+int(user_id[8])*int(second_module[8])+int(user_id[9])*int(second_module[9])
print(result_sum2)
check_number=user_id[10]
print(check_number)
control_function=result_sum%11
print(control_function)
control_function2=result_sum2%11
print(control_function2)
if control_function<10:
    if control_function==int(check_number):
     print ('ID code is correct')
    else:
        print('Please check Your ID code')
else:
    if control_function2<10:
        if control_function2==int(check_number):
            print ('ID code is correct')
        else:
            print('Please check Your ID code')
    else:
        if check_number==0:
            print ('ID code is correct')
        else:
            print ('Please check Your ID code')





