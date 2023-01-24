# Insertion Sort in Python

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array [j - 1]
            j -= 1
        
array = [77, 29, 18, 6, 37, 86, 39, 50, 55, 97]
insertion_sort(array)

print(array)