while True:
    user_input=input('Please enter your ID: ')
    # print(int(user_input))
    try:
        user_input=str(int(user_input))
        if len(user_input) !=11:
            raise UserWarning  # raise вызываем какие-нибудь ошибки
        else:
            condition=False
    except ValueError:
        print('Raised error')
    except UserWarning:
        print('ID code is too short or too long')
    else:
        print('Your national id is', user_input)
    finally:  #finally выполняет код внутри себя
        print('Program finished working!')