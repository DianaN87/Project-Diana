set1={'Math', 'History', 'Programming', 'Physics', 'Math'}
set2={'Art', 'Physics', 'Design', 'History'}

print (set1) # хранит в себе все уникальные значения, повторы удаляет
list1=['Math', 'History', 'Programming', 'Physics', 'Math', 'History']
print (list1)
print(type(list1))
print(list(set(list1)))

#intersection () method returns a set of intersection between two sets
print(set1.intersection(set2))
# difference () method returns a set of differences in two sets
print(set2.difference(set1)) # chem set2 otlichaetsja ot set1
print(set1.difference(set2))

#union ()method will return a set of all value from both sets
print(set1.union(set2))