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

'''
Merge Sort
Merge Sort is able to sort an order of magnitude better than the previous sorts like selection and insertion sort. Remember binary search, and how it was able to search quickly? Merge sort is similar in that it keeps splitting the array in half, and recursively sorting each half. If you keep splitting in half like this, you'll eventually have only 1 or 2 elements. It's easy to sort a short array like this, with basically only 1 operation!

So, it's easy to sort small arrays, but how do we recombine the tiny sorted arrays into the original array? This is where Merge Sort gets its name, in merging the two sorted sub-arrays.

Let's first focus on the logic of merging two sorted arrays, into one sorted array.

# Consider two lists (that are already sorted):
A, D, F         B, C, E

# First set a marker at the start of each:
A, D, F         B, C, E
^               ^

# Compare the values at each marker
# Add the lower value (if ascending) to the new list (on the right)
# And increment that marker
A, D, F         B, C, E       A
   ^            ^

# Repeat until one of the markers leaves its list
A, D, F         B, C, E       A, B
   ^               ^

A, D, F         B, C, E       A, B, C
   ^                  ^

A, D, F         B, C, E       A, B, C, D
      ^               ^

A, D, F         B, C, E       A, B, C, D, E
      ^                 ^

# Once one marker is done, just move the
# remaining part of the other list straight over
A, D, F         B, C, E       A, B, C, D, E, F
        ^               ^

# Now you have a sorted list!
A, B, C, D, E, F
  
Take the time to re-read the last part if you are still a bit confused. Merge Sort won't make sense without understanding this part first. You can also try doing it on paper to get the hang of it.

Now that we understand the merge part of Merge Sort, we need to put all this information into a single algorithm.

There are two markers for Merge Sort:

Marker A marks the first merge list
Marker B marks the second merge list
Purple slots are outside the current range. Plain cells are in the current recursive call.
Basically the algorithm recursively does one of the following:

Sorts a tiny array (Base case)
Split in half
Recursive call on first half
Recursive call on second half
Merge the two
Below are some visualizations of Merge Sort. Hit play, or keep stepping through to see how the markers move, and items are swapped.

There are print statements to help see how different parts of the array are sorted at each step. Take the time to read this program and output line by line. Future classes will expect you to be able to write merge sort by hand. (But not in this class).

Once you understand the basic algorithm in theory, the hardest part is getting all the indexing correct in practice. There's a lot of adding and subtracting 1 to get the right index.

Can you tweak the above program to sort in descending order? You should have a function named merge_sort that takes at least 1 parameter array. It should sort the array using merge sort, and in descending order. Then it should print out the array.

Here is an example with merge_sort([9, 5, 3, 6, 8, 1, 0, 2, 4, 7]):

Can you figure out O() of Merge Sort? Hint: it is better than O(n2).

First, the algorithm keeps splitting the array in half each time. This is O(log(n)). Then for each of those splits, it does a merge. What is the O() of the merge? Since the two markers only go to each end of their array, AND the total length of each array is never more than the total length of the original array, then the markers move no more than O(n) times. In essence we have an outer loop of O(log(n)) and an inner loop of O(n), so the result is O(n log(n)). Remember, O(n log(n)) is better than O(n2).'''