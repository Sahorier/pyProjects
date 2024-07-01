# Project HELLO MASTER
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hh = int(time.strftime('%H'))
mm = int(time.strftime('%M'))
ss = int(time.strftime('%S'))
if (hh >= 6 and hh <12):
    print("Good morning Master RH!")
elif (hh >= 12 and hh < 16):
    print("Good noon Master RH!")
elif (hh >=16 and hh < 18 ):
    print("Good afternoon Master RH!")
else:
    print("Good night Master RH!")