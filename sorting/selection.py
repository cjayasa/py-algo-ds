def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(len(array) - i):
            if array[j+i] < array[min_index]:
                min_index = j+i
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array

if __name__ == "__main__":
    array = [4, 2, 7, 9, 1, 14, 6, 8, 2]
    selection_sort(array)
    print(array)