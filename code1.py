import random
Names = ["Lisa", "John", "Mike", "Sarah", "Kate", "Tom", "Anna", "James", "Laura", "David"]
Name = random.choice(Names)
Marks = random.randint(0, 100)
# print(f"{Marks} , {Name}")
if Marks >= 90:
    print("You are a good student:")
elif Marks >= 70:
    print("You are a good student but you can do better however i am pround of you keep improving:")
elif Marks >= 50:
    print("You need to work hard:")
else:
    print("You are faild in exam:")  
    reason =  input("What's the reason your failed in exam:")
    if reason == "sickness" or reason == "family issues" or reason == "anything else": 
        print('okay')
    else:
        print("You should have studied more:")
print(f"{Name} , {Marks}")