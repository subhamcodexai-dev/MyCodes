# __________________TEMPERATURE TRACKER______________________

def temp_time():
    temp = []
    temp.append(("Morning" , 34))
    temp.append(("Afternoon" , 333))
    temp.append(("Evening"  , 23))
    temp.append(("Night" , 234))
    return temp

temperature = temp_time()

names , numbers = zip(*temperature)

for name , number in zip(names,numbers):
    print(f"{name}: " , f"{number}")

average = sum(numbers) / len(numbers)
highest = max(temperature)
lowest = min(temperature)

print(temperature)
print(average)
print(highest)
print(lowest)