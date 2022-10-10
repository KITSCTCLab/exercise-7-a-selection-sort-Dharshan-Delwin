from typing import List

def selectionSort(array, size) -> List[int]:
    for y in range(len(array)):
      min_idx = y
      for j in range(y+1,len(arr)):
        if array[min_idx] > array[j]:
          min_idx = j
       array[y], array[min_idx] = array[min_idx],array[y]
    return array
      
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
