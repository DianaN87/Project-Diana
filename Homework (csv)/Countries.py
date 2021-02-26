import csv
with open('2019.csv','r', encoding='UTF8') as csv_file:
    csv_reader=csv.reader(csv_file)
    valuables=list(csv_reader)[2:]
    TOP10=10
    GDP=sorted(valuables,key=lambda x: x[3],reverse=True)[:10]
    Social_support=sorted(valuables, key=lambda x:x[4],reverse=True)[:10]
    Freedom_to_make_life_choices=sorted(valuables, key=lambda x:x[4],reverse=True)[:10]
    # print('The list of TOP10 countries with highest GDP per capita:\n'+str(GDP))
    # print('The list of TOP10 countries with highest index "Social support":\n' +str(Social_support))
    # print('The list of TOP10 counties with highest index "Freedom to make life choices\n'+ str(Freedom_to_make_life_choices))
with open('list_of_countries.csv', 'w') as new_file:
    fieldnames=['Country','GDP per capita']
    csv_writer=csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
    csv_writer.writeheader()
    csv_writer.writerow({'Country': GDP[:][:][1],'GDP per capita':GDP[:][:][1]})
print(len(GDP))
print(GDP[:][:][1])
# print(GDP)
# print (type(GDP))
