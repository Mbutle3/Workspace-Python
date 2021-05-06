def FindSmallest(array):
    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def SelectionSort(array):
    new_array = []
    for i in range(len(array)):
        smallest = FindSmallest(array)
        new_array.append(array.pop(smallest))
    return new_array


print(SelectionSort([5, 3, 6, 2, 10]))
