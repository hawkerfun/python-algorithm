def binarySearch(arr, target, left, right):
  random_pos = 0
  while True:
    if left > right or random_pos == (right + left) // 2:
      return -1
    
    random_pos = (right + left) // 2
    if target > arr[random_pos]:
      left = random_pos
      continue

    if target < arr[random_pos]:
      right = random_pos
      continue

    if target == arr[random_pos]:
      return random_pos