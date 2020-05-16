def partition(arr, low, high):
  i = (low - 1)
  pivot = arr[high]

  for j in range(low, high):
    if pivot > arr[j]:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i+1], arr[high] = arr[high], arr[i+1]

  return (i + 1)

def quickSort(arr, low, high):
  if low < high:

    pi = partition(arr, low, high)
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)


  return arr  

""" ================== Walkthrough and Debug ================== """
# 1, 5, 8, 9, 10, 7
# ==============
# 1, 5, 7, 9, 10, 8
# ==============
# 1, 5, 7, 9, 10, 8