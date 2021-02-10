courses= ['Math', 'Histore', 'Programming', 'Physics', 'Art', 'Biology']

for subject in courses:
    print(subject) # object- все, что внутри скобок

counter=0
for subject in courses:
    print(subject)
    print(subject)
    counter+=1 #пересчитывает
print(counter)

courses='Hello world'
counter=0
for subject in courses:
    print(subject)
    counter +=1
print(counter)
courses= range (0,100)
counter=0
for subject in courses:
    print(subject)
    counter +=1
print(counter)

courses=[0,1,2,3,4,5,6,7,8,9]
counter=0
for num1 in courses:
    for num2 in courses:
        for num3 in courses:
            for num4 in courses:
                print(num1, num2,num3, num4)

courses=['one', 'two', 'three']
counter=0
for num1 in courses: # num1 - mozet bit nazvan kak ugodno, programma ponimajet, chto eto pervi element v spiske
    for num2 in courses:
        for num3 in courses:
            for num4 in courses:
                print(num1, num2,num3, num4)
courses='Hello world'
counter=0
for subject in courses:
    print(courses)

numbers= range(1,101)
for num in numbers:
    if num % 2==0: # % ostatok pri delenii
        print(num, 'Even')
    else:
        print(num,'Odd')

numbers=range(1,101)
for num in numbers:
    if num % 5 == 0 and num % 3 == 0:
        print (num, 'FizzBuzz')
    elif num % 5 == 0:
        print(num, 'Fizz')
    elif num % 3 == 0:
        print(num, 'Buzz')

counter =0
for num1 in numbers:
    print(num1)
counter+=100
print(counter)

counter =0
for num1 in numbers:
    print(num1)
    counter+=100
print(counter)
