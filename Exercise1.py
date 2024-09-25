
numbers: list[int] = []

for i in range(1, 100 + 1):
    numbers.append(i)
print(numbers)
print(numbers[0])
print(numbers[-1])
print([len(numbers)])
print(numbers[2:12])
print(numbers[80:])
print(numbers[:18])
print(numbers[::-1])
print(numbers[1:100:2])
print(numbers[2:100:3])
print(numbers[6:100:7])
print(numbers[9:100:10])
print(numbers[-2:63:-3])
numbers.insert(50,999)
print(numbers)
numbers.pop(100)
print(numbers)


