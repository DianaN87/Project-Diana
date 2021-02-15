import calendar
print(calendar.month(2020,11, w=10, l=0)) # esli 1-9 mecjaz, to nuzno pisat prosto chslo bez 0 speredi
print(calendar.calendar(2020, w=0, l=0, c=13, m=3)) # c=3 - rastojanie mezdu stolbikami vsego kalendarakolichestvo, m- kolichestvo mesjacev v odnu strochku
print(calendar.weekday(2021, 2, 15)) # 0 pokazaivajet po indeksu denj nedeli v formate chisla
print(calendar.isleap(2020)) # will return True because 2020 is a leap year
print(calendar.isleap(2018)) # will return False because 2018 is not a leap year

print(calendar.leapdays(2000,2021)) # will return number of leap years between 2000 and 2020
