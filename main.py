def insertion_sort(arr):
  """
  Sorts an array using insertion sort algorithm.

  Args:
      arr: The input array to be sorted.

  Returns:
      The sorted array.
  """
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    # Move elements greater than key one position ahead
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr

# Example usage
my_list = [7, 4, 5, 2]
sorted_list = insertion_sort(my_list)
print(sorted_list)  # Output: [2, 4, 5, 7]
