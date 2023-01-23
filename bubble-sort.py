# Bubble Sort in Python
 
def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                temp_var = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp_var

    # print(array)
    # Code above can be used to observe the process of Bubble Sort Algorithm

array = [77, 29, 18, 6, 37, 86, 39, 50, 55, 97]
bubble_sort(array)

print(array)