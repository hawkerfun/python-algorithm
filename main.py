from SearchingAlgorithms.BinarySearch import binarySearch
#from SortingAlgorithms.SortingWithInsertion import sortWithInsertion
from SortingAlgorithms.QuickSort import quickSort

arr = [ 10, 7, 8, 9, 1, 5 ]
arr = quickSort(arr, 0, len(arr) - 1)
print(arr)
pos = binarySearch(arr, 8, 0, len(arr))
print(pos)