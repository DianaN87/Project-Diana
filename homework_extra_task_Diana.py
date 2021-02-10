first_option=input('Please press 1 to insert id code or 0 to exit')
if float(first_option)==1:
    id_code= input ('Please enter Your national id: ')
    if len(id_code)==11:
        day=id_code[5:7]
        month=id_code[3:5]
        if float(id_code[0])==3 or float(id_code[0])==4:
            birth_date=day+"."+month+"."+"19"+id_code[1:3]
            print(birth_date)
        else:
            birth_date=day+"."+month+"."+"20"+id_code[1:3]
            print(birth_date)
        if id_code[0]=='3' or id_code[0]=='5':
            print ('Man')
        elif id_code[0]=='4' or id_code[0]=='6':
            print('Woman')
        else:
            print('Please check your first number')
        place_of_birth=float(id_code[7:10])
        if float(place_of_birth)>1 and float(place_of_birth)<10 or float(place_of_birth)==10:
            print ('Kuressaare haigla')
        elif float(place_of_birth)>11 and float(place_of_birth)<19 or float(place_of_birth)==19:
            print ('Tartu Ülikooli Naistekliinik')
        elif float(place_of_birth)>19 and float(place_of_birth)<150 or float(place_of_birth)==150:
            print ('Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja (Tallinn)')
        elif float(place_of_birth)>150 and float(place_of_birth)<160 or float(place_of_birth)==160:
            print ('Keila haigla')
        elif float(place_of_birth)>160 and float(place_of_birth)<220 or float(place_of_birth)==220:
            print ('Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)')
        elif float(place_of_birth)>220 and float(place_of_birth)<270 or float(place_of_birth)==270:
            print ('Ida-Viru Keskaigla (Kohtla-Järve, endine Jõhvi)')
        elif float(place_of_birth)>270 and float(place_of_birth)<370 or float(place_of_birth)==370:
            print ('Maarjamõisa kliinikum (Tartu), Jõgeva haigla')
        elif float(place_of_birth)>370 and float(place_of_birth)<420 or float(place_of_birth)==420:
            print ('Narva Haigla')
        elif float(place_of_birth)>420 and float(place_of_birth)<470 or float(place_of_birth)==470:
            print ('Pärnu haigla')
        elif float(place_of_birth)>470 and float(place_of_birth)<490 or float(place_of_birth)==490:
            print ('Haapsalu haigla')
        elif float(place_of_birth)>490 and float(place_of_birth)<520 or float(place_of_birth)==520:
            print ('Järvamaa haigla')
        elif float(place_of_birth)>520 and float(place_of_birth)<570 or float(place_of_birth)==570:
            print ('Rakvere haigla, Tapa haigla')
        elif float(place_of_birth)>570 and float(place_of_birth)<600 or float(place_of_birth)==600:
            print ('Valga haigla')
        elif float(place_of_birth)>600 and float(place_of_birth)<650 or float(place_of_birth)==650:
            print ('Viljandi haigla')
        elif float(place_of_birth)>650 and float(place_of_birth)<700 or float(place_of_birth)==700:
            print ('Lõuna-Eesti haigla (Võru), Põlva haigla')
        else:
            print ('not specified')
    elif len(id_code)>11:
        print('Code You entered is longer than 11 digits')
    else:
        print('Code You entered is shorter than 11 digits')
elif float(first_option)==0:
    exit()