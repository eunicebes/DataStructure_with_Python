numbers = [1, 4, 10, 3, 5, 30, 21, 22, 15, 8]

def heapify(numbers, n, i):
    largest = i
    left =  2 * i + 1
    right = 2 * i + 2

    if left < n and numbers[i] < numbers[left]:
        largest = left

    if right < n and numbers[largest] < numbers[right]:
        largest = right

    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        heapify(numbers, n, largest)

def heapsort(numbers):
    n = len(numbers)

    for i in range(n-1, -1, -1):
        heapify(numbers, n, i)

    for i in range(n-1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)

    print(numbers)


heapsort(numbers)