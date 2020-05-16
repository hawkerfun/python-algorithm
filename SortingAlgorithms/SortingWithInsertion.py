def sortWithInsertion(arr, len):
  new_list = arr.copy()
  
  for i in range(1, len):
    temp = new_list[i]
    curr_pos = i - 1

    while temp < new_list[curr_pos] and curr_pos > -1:
      new_list[curr_pos + 1] = new_list[curr_pos]
      curr_pos -= 1
    
    new_list[curr_pos + 1] = temp
  
  return new_list 