# Insertion Sort in Python

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array [j - 1]
            j -= 1
        
        # print(array)
        # Code above can be used to observe the process of Insertion Sort Algorithm

array = [2, 6, 5, 1, 3, 4]
insertion_sort(array)

print(array)