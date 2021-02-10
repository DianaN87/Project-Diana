id_code= input ('Please enter Your national id: ')
if len(id_code)==11:
    day=id_code[5:7]
    month=id_code[3:5]
    if id_code[0]==4 or 5:
        birth_date=day+"."+month+"."+"19"+id_code[1:3]
        print(birth_date)
    else:
        birth_date=day+"."+month+"20"+id_code[1:3]
        print(birth_date)
    if id_code[0]=='3' or id_code[0]=='5':
        print ('Man')
    elif id_code[0]=='4' or id_code[0]=='6':
        print('Woman')
    else:
        print('Please check your first number')
    if id_code[8:10]>1 and id_code[8:10]<10 or id_code[8:10]==10:
        print ('Kuressaare haigla')
    elif id_code[8:10]>'11' and id_code[8:10]<'19'or id_code[8:10]='19':
        print ('Tartu Ülikooli Naistekliinik')
elif len(id_code)>11:
    print('Code You entered is longer than 11 digits')
else:
    print('Code You entered is shorter than 11 digits')

