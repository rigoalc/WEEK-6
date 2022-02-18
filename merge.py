def swap(array, index1, index2):
    """Swap values at given indexes in given array (same function as before)"""
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def do_merge(array1, array2):
    print("do_merge({}, {})".format(array1, array2))
    merged = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1
    # Add remaining
    if array1:
        merged.extend(array1[i:len(array1)])
    if array2:
        merged.extend(array2[j:len(array2)])
    print("Merged:", merged)
    assert len(merged) == len(array1) + len(array2)
    return merged

def merge_sort(array, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1
    print("{}:{} = {}".format(start, end, array[start:end+1]))
    if end - start <= 0:
        return # Nothing to sort
    elif end - start == 1:
        # Sort once
        if array[start] > array[start+1]:
            swap(array, start, start+1)
        return # Sorted
    else:
        # Sort left half and right half recursively
        middle = start + int((end - start) / 2)
        merge_sort(array, start, middle)
        merge_sort(array, middle+1, end)
        # Then merge
        merged = do_merge(array[start:middle+1], array[middle+1:end+1])
        # Put back into array
        for i, value in enumerate(merged):
            array[start+i] = value

numbers = [9, 5, 3, 6, 8, 1, 0, 2, 4, 7]
print(numbers) # Print before
merge_sort(numbers)
print(numbers) # Print after