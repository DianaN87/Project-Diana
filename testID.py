id_code = input('Please enter Your national id: ')
def id_check(id_code, chk_list):
    counter = 0
    result = 0
    for num in chk_list:
        result += int(id_code[counter]) * num
        counter += 1
    return result % 11
    print(result)
    id_code_list = list(id_code)
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