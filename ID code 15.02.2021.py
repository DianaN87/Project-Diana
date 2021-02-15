condition=True
while condition:
    first_option = input('Please choose:\n1.Check id code\n0. Exit\n -->')
    if float(first_option) == 1:
        condition2 = True
        while condition2:
            id_code = input('Please enter Your national id: ')
            try:
                id_code = str(int(id_code))
                if len(id_code) !=11:  #!= - ne javljaetsja
                    if len(id_code)>11:
                        #print('ID code you entered is too long or too short')
                        print('ID code is too long')
                    elif len(id_code)<11:
                        print ('ID code is too short')
                    raise UserWarning
                else:
                    condition2=False
            except:
                print('ERROR')
            else:
                condition3= True
                while condition3:
                    try:
                        def id_check(id_code, chk_list):
                            counter = 0
                            result = 0
                            for num in chk_list:
                                result += int(id_code[counter]) * num
                                counter += 1
                            return result % 11
                            print (result)
                        id_code_list= list(id_code) #ecli ne napechatatj etot input, to budet bezat postojanno strochka
                        chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                        chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                        if id_check(id_code_list, chk1) == 10:
                            result = id_check(id_code_list, chk2)
                            print(result)
                            if result == int(id_code_list[10]):
                                print('ID code is valid SSS')
                            elif int(id_code_list[10]) == 0:
                                print('ID code is OK')
                            else:
                                print('ID code is invalid VVV')
                        elif id_check(id_code_list, chk1) == int(id_code_list[10]):
                            print('ID code is valid ttt')
                        else:
                            condition3=False
                    except:
                        print('ERROR1')
                    else:
                        # Create variables for parts of ID code
                        gender_id = (id_code[0])
                        birth_year = (id_code[1:3])
                        birth_month = (id_code[3:5])
                        birth_day = (id_code[5:7])
                        birth_region = (id_code[7:10])
                        check_num = (id_code[10])
                        # IF statement to check gender and century of birth
                        if gender_id == '1':
                            gender = 'Male'
                            birth_cent = '18'
                        elif gender_id == '2':
                            gender = 'Female'
                            birth_cent = '18'
                        elif gender_id == '3':
                            gender = 'Male'
                            birth_cent = '19'
                        elif gender_id == '4':
                            gender = 'Female'
                            birth_cent = '19'
                        elif gender_id == '5':
                            gender = 'Male'
                            birth_cent = '20'
                        elif gender_id == '6':
                            gender = 'Female'
                            birth_cent = '20'
                        else:
                            gender = 'unknown'
                            birth_cent = 'unknown'

                        if int(birth_region) in range(1, 11):
                            region = 'Kuressaare haigla'
                        elif int(birth_region) in range(11, 20):
                            region = 'Tartu Ülikooli Nastekliinik'
                        elif int(birth_region) in range(21, 151):
                            region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
                        else:
                            region = 'unknown'
                        print('Your national id is: ' + id_code)
                        print('You are ' + gender)
                        print('Your date of birth is: ' + birth_day + "." + birth_month + "." + birth_cent + birth_year)
                        print('You are born in ' + region)
                                    # pass -временно используется, для пропуска, ничего не делать
    elif first_option == '0':
        quit('Program has quit working')
    else:
        print('Choice out of range!')
