with open('Alice', 'r', encoding='UTF8') as file:
    text=file.read().lower().replace(',','').replace('.','').replace('?','').replace('!','').replace(':','').replace(";","").replace("\n"," ")
    text_list=text.split(" ")
print(text_list)

print(len(text_list))
print(len(set(text_list)))

#or

unique=[]
for word in text_list:
    if word not in unique:
        unique.append(word)
print(len(unique))

with open('count', 'w', encoding='UTF8') as file:
    file.write('There are '+str(len(text_list))+' words in text file.\n')
    file.write('There are '+str(len(set(text_list)))+' unique words in the text file.')



