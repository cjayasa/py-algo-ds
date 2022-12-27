def bubble_sort(array):
    sorted = False
    while not sorted:
        i = 1
        swapped = False
        while i < len(array):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                swapped = True
            i += 1
        if not swapped:
            break;
    return array

if __name__ == "__main__":
    array = [4, 2, 7, 9, 1, 14, 6, 8, 2]
    bubble_sort(array)
    print(array)