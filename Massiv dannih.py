# empty_string=""
# print(type(empty_string))
#
# empty_list=[]
# print(type(empty_list))
#
# empty_tuple = ()
# print(type(empty_tuple))
#
# empty_set = set()
# print(type(empty_set))
#
# some_list =[12335, 123.0023,'Some string', True, None, [1234, 'New string', False]]
# print(some_list)
#
# print(some_list[0:3])
# print(some_list[-1])
# print(some_list[::-1])
# print(type(some_list[0]))
#
# courses =['History', 'Math', 'Literature', 'Physics', 'Programming']
# print(courses)
# courses[2]='Art'
# print(courses)
#
courses = ['History', 'Math', 'Literature', 'Physics', 'Programming',[1,2,3,4,5]]
# print(courses[5][4])
# courses[2] = 'Litera'
# print(courses)
#
# print(len(courses))
#
# print(len(courses[5])) #dlina otdelnogo elementa
#
# courses2 = ['Art', 'Biology']
# print(courses + courses2)
#
# courses.append('Art') #append- dobavljaet element
# print(courses)
#
# courses.append(courses2)
# print(courses)
#
# courses[5].append(courses2)
# print(courses)
# print(courses[5][5][1])
#
# print (courses)
# courses.remove('Math')
# print(courses)

# courses.pop()
# print(courses)
# popped_item= courses.pop()
# popped_item2=courses.pop()
# print(courses)
# print(popped_item)
# print(popped_item2)
#
# courses=['History', 'Math', 'Literature', 'Physics', 'Programming']
# courses2=['Art', 'Biology']
# print(courses)
# courses.insert(2, 'Biology')
# print(courses)
#
# print (courses)
# courses.extend(courses2)
# print(courses)

courses= ['History', 'Math', 'Literature', 'Physics', 'art', ' Programming','123','534']
numbers=[1,45,63,34,56,78,3]
courses2=['Art', 'Biology']

print(numbers)
numbers.sort()
print(numbers)

print(courses)
courses.sort()
print(courses)

courses.sort(reverse=True) #sortirovka v obratnom porjadke
print(courses)
courses.sort(reverse=False)
print(courses)

option=True  # zadaem peremennuju
courses.sort(reverse=option)
print(courses) # poljzovatelj mozet postavit galochku i togda budet True

print(sorted(courses)) #mi odin raz v konkretni moment sortirujem
print(courses)

print(min(numbers))
print(max(numbers))
print(min(courses))
print(max(courses))
print(sum(numbers))
print(courses.index('Math'))

print(courses.index('Math'))
print (courses)
max_index=courses.index('Math')
print(courses[max_index])

print('art' in courses)
if 'art' in courses:
    print('GOOD')
else:
    print('BAD')

courses= ['History', 'Math', 'Literature', 'Physics', 'art', ' Programming','123','534']
numbers=[1,45,63,34,56,78,3]
courses2=['Art', 'Biology']

new_string= ', '.join(courses) #pokazivajem kakim obrazom sojedinit eti stroki
print(new_string)
print(type(new_string))

new_list =new_string.split (' , ')
print(new_list)
print(type(new_list))

# new_list=some_string.split('\n') # \n - perenos stroki, napechatajet, gde est perenosi strok

list_1=['Math', 'History', 'Programming','Physics']
list_2=list_1.copy() # metod kopii, vsegda budet k ishodnomu vozvrashatsja
list_2.insert(2, 'Biology')

print(list_1)
print(list_2)

list_1[2]='Sports'
list_2[0] ='Art'
print(list_1)
print(list_2)

