numbers = [1, 3, 10, 4, 31, 22, 2, 5, 11, 8]

for i in range(1, len(numbers), 1):
    current_num = numbers[i]
    for j in range(i-1, -1, -1):
        if current_num < numbers[j]:
            numbers[j+1] = numbers[j]
        else:
            numbers[j+1] = current_num
            break

print(numbers)