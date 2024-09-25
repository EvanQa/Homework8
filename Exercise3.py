numbers = [i for i in range(10, 101, 10)]
while True:
    user_input = int(input("enter a number : (for break enter -999) "))
    if user_input == -999:
        break
    numbers.append(user_input)
    numbers.sort()


print("The sorted list: ", numbers)
