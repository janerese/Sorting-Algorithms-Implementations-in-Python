# Selection Sort using Python

def selection_sort(array):
    for i in range(5):
        min_position = i
        for j in range(i, 6):
            if array[j] < array [min_position]:
                min_position = j

        temporary = array[i]
        array[i] = array[min_position]
        array[min_position] = temporary

        print(array)
        
array = [5, 3, 8, 6, 7, 2]
selection_sort(array)

print(array)