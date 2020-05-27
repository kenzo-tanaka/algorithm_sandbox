def binary_search(list, item):
  low = 0
  high = len(list) -1
  while low <= high:
    mid = (low + high) / 2
    guess_item = list[mid]
    if item == guess_item:
      return guess_item
    if guess_item > item:
      high = mid - 1
    else:
      low = mid + 1


list = [1,3,5,9,10,33,99,100]

print binary_search(list, 3)
print binary_search(list, 5)