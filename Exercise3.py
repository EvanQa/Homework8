my_list = list(range(10,101,10))
print(my_list)
while True:
    numbers: int = int(input('enter a number'))
    if numbers == -999:
        break
for i in range(len(numbers)):
        if numbers < my_list[i]:
            my_list.insert(i, numbers)
        print(my_list)
