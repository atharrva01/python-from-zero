import time


hour = int(time.strftime("%H"))
min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))

print("Its been: " , hour,"hours")
print("and this: " , min , "minutes")
print(sec)

if(hour > 12):
    print("Good Morning Sir")
elif (12 == hour < 17):
    print("Good After Sir")
else :
    print("GOOD NIGHT")
