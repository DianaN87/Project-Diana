empty_string = ''
string_sample = "Hello world world"
string_sample2 = "first letteR is lowErcase"
string_sample3 = " extra whitespace string"
german_sample = "der FluS"

print (string_sample [0])
print (string_sample [0:5])

print (string_sample [-1])
print (string_sample [-5:-1]) # -5 is not taken into account
print (string_sample [-5:]) # if is empty escape, than it will take all values till the end of string
print (string_sample [ :5])
print (string_sample [:])
print (string_sample [0: :2]) # path- each second
print (string_sample [::-1])

test_string = "Hello world. It is beautiful day."
print (test_string [0:11])
print (test_string [-4:-1])
print (test_string [0:5], test_string[19:29])

print (len(test_string))
print (test_string.find('beautiful'))
print(len('beautiful'))
print (test_string[19:28])

print(test_string.upper())
print (test_string.split())
print(test_string[0:5].upper())
print (test_string[0:5],test_string [5:0])
print (german_sample.lower())
print (german_sample.casefold())
print(string_sample2.capitalize())

user_name= "rOman"
print(user_name.lower().capitalize())
print(user_name.capitalize().lower())
print (user_name)


user_name=user_name.lower().capitalize()
print(user_name)

print (string_sample.find('world')) #index from which starts "world"
print (string_sample.count('world'))
print (string_sample[0:7].count('world'))
search_string= 'world'
print(string_sample.count(search_string))

print('world' in string_sample) # sushetvujet li eto slovo v stroke

print(string_sample + " " + string_sample2)
print (string_sample, ".", string_sample2)
salary=1000
worker_string="John's salary is"
print(worker_string, salary)

worker = 'John'
worker2='Mary'
salary=1000
salary2=2000
worker_string= "'s salary is"
print (worker+worker_string, salary)
print (worker2+worker_string, salary2)

print("{}'s salary is {}".format(worker, salary))

worker_string="{}'s salary is {}"
print (worker_string.format(worker, salary))
worker_string="{1}'s salary is {0}" #indeksacija
print (worker_string.format(worker, salary))

apples=3
bananas=5
pears=2
fruit_string="John has {} bananas, {} apples and {} pears"
print(fruit_string.format(bananas, apples, pears)) #many arguments can be given

fruit_string2="John has {1} bananas, {0} apples and {2} pears"
print (fruit_string2.format(bananas, apples, pears)) #Index can be used as a placeholder

price_string="This {product:} costs {price: .2f} euros"
print(price_string.format(price=350, product="computer")) #.2f stands for 2 numbers after decimal point f - float
price_string="This {product:} costs" +str(float()) {price: .2f} euros"