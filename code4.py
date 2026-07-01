fruits = []
toys = []
materials = []
amount = 0
for i in range(1):
    f = input("what fruits you bought from market:")
    fruits.append(f)
    if f == "mango":
        amount += 20
        print("mango:20")
    elif f == "apple":
        amount += 10
        print("apple:10")
    else:
        print("error")
    t = (input("what toys you bought from market:"))
    toys.append(t)
    if t == "robot":
        amount += 150
        print("robot:150")
    elif t == "car":
        amount += 250
        print("car:250")
    else:
        print("error")
    m = input("what materials you bought from market:")
    materials.append(m)
    if m == "hammer":
        amount += 200
        print("hammer : 200")
    elif m == "steel":
        amount += 400
        print("steel = 400")
    else:
        print("error")
print(f"{amount}")
nameoftheitems = (f"{fruits} , {toys} , {materials}")
print(nameoftheitems)