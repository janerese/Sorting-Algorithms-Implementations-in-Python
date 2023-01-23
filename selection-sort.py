# Selection Sort in Python

def selection_sort(array):
    for i in range(9):
        min_position = i
        for j in range(i, 10):
            if array[j] < array [min_position]:
                min_position = j

        temp_var = array[i]
        array[i] = array[min_position]
        array[min_position] = temp_var

        print(array)

array = [77, 29, 18, 6, 37, 86, 39, 50, 55, 97]
selection_sort(array)

print(array)