# # while True: # po umolcaniju  vsegda istina, while trebujet kakogo-to starta
# #     print("I can't stop!!!")
# counter=0
# while counter<100:
#     print("I can't stop!!!",counter, 'times')
#     counter+=1  # toze samoje chto counter=counter+1
# counter=0
# while counter<=10000:
#     counter+=1
#     if counter %100==0:
#         print(counter)
# condition=True
# while condition:
#     user_input= input('Please enter id: ')
#     if len(user_input) !=11:
#         print ('Please try again')
#     else:
#         print (user_input)
#         condition=False

while True:
    user_input= input('Please enter id: ')
    if len(user_input) !=11:
        print ('Please try again')
        continue  # govorit, prodolzai zikl
    else:
        print(user_input)
        break  #govorit, razorvi zikl