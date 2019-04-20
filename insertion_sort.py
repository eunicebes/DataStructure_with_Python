numbers = [3, 1, 10, 4, 31, 22, 2, 5, 11, 8]

for i in range(1, len(numbers), 1):
    current_num = numbers[i]
    for j in range(i-1, -1, -1):
        if current_num < numbers[j]:
            numbers[j+1] = numbers[j]
            numbers[j] = current_num

print(numbers)