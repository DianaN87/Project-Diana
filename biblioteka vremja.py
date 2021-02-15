# import time
# start=time.time()
# time.sleep(7) #vizivajet iskustvennuju zaderzku v 7 secund, kak programma doshla do etogo
#
# end=time.time() #time.time()- will return tie now vremja seichas
# print(end-start)
#
# import time
# print(time.asctime())
# print(time.gmtime())
# print(type(time.gmtime()))
import time
date_now=time.gmtime()
print (date_now[0], date_now[1], date_now[2])

import datetime

d=datetime.date(2018, 7, 22) # data, kotoruju mi hotim zadat sami, t.e. mi sozdajem objekt dati
print (d)
print(type(d))

today=datetime.date.today() # vizivajetsja toljko data, bez vremeni
print(today)

d=datetime.date(2000, 6, 15)
today=datetime.date.today()
print(today-d)

print(today.year)
print(today.month)
print(today.month)
print(type(today.month))

print(d.year)
print(d.month)
print(d.month)
print(type(d.month))

print(today.weekday()) #Monday 0 Sunday 6
print(today.isoweekday()) #Monday 1 Sunday 7

today=datetime.date.today()
delta=(datetime.timedelta(days=7))
print(today+delta)

today=datetime.date.today()
bday=datetime.date(2021,5,18)
till_bday=bday-today
print(till_bday) #will return days and hours until bday
print(till_bday.days)
print(till_bday.total_seconds())

t=datetime.time(13,24,10,10)
print(t) # Will print time with all parameters

dt=datetime.datetime(2020,11,30,18,20,36,100000)
print(dt)
print(dt.date()) #will print date only
print(dt.time()) #will print time only

dt_delta=datetime.timedelta(days=7, hours=15, minutes=10)
print(dt+dt_delta) #Will print datetime after delta

dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
print(dt_today)
print(dt_now)

print(dt_today.strftime('%B %d, %Y')) #will print formated date where %B is full month, %d as number, %T year in YYYY format

dt_str='November 30, 2020'
dt_str='Nov 30, 2020'
str_to_date=datetime.datetime.strptime(dt_str, '%b %d, %Y') # Converts string into datetime format
print(str_to_date)
print(type(str_to_date))