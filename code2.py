import random
characters = ('abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*')
digits = "892374"
length = int(input("enter length for your password"))
password =""
if length >= 10:
  chars = characters  + digits
elif length >= 5:
  chars = characters + digits
elif length >= 3:
  chars = characters + digits
else:
  chars = characters + digits
for i in range(length):
    password += random.choice(chars)
print(password)