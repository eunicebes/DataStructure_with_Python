numbers = [1, 4, 10, 3, 5, 30, 21, 22, 15, 8]

def mergeSort(input_list):
    print("splitting", input_list)
    if len(input_list) > 1:
        mid_point = len(input_list)//2
        left_list = input_list[:mid_point]
        right_list = input_list[mid_point:]

        # do recurrence
        mergeSort(left_list)
        mergeSort(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                input_list[k] = left_list[i]
                i = i + 1
            else:
                input_list[k] = right_list[j]
                j = j + 1

            k = k + 1

        while i < len(left_list):
            input_list[k] = left_list[i]
            i = i + 1
            k = k + 1

        while j < len(right_list):
            input_list[k] = right_list[j]
            j = j + 1
            k = k + 1

    print("merging", input_list)

mergeSort(numbers)