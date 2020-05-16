from SearchingAlgorithms.BinarySearch import binarySearch
from SortingAlgorithms.SortingWithInsertion import sortWithInsertion

arr = [ 2, 12, 4, 101, 98 ]
arr = sortWithInsertion(arr, len(arr))
print(arr)
pos = binarySearch(arr, 101, 0, len(arr))
print(pos)