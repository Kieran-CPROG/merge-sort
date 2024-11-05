#Kieran Uptagrafft
#10/31/24
#Merge sort


def merge_sort(unsorted):
  sorted = []

  if len(unsorted) == 1:
    return unsorted

  temp = int(len(unsorted) / 2)
  left = merge_sort(unsorted[:temp])
  right = merge_sort(unsorted[temp:])

  x = 0
  y = 0
  left_len = len(left)
  right_len = len(right)
  
  while x != left_len or y != right_len:
    if x != left_len and (y == right_len or left[x] < right[y]):
        sorted.append(left[x])
        x += 1
    else:
        sorted.append(right[y])
        y += 1

  
  return sorted

def main():
    nums1 = [6,2,5,8,3,4,8]
    nums2 = [1,2,3,4,5,6,7,8]
    nums3 = [8,2,6,0,1,3]

    for num_list in [nums1, nums2, nums3]:
        print(f"\nOriginal: {num_list}")
        new = merge_sort(num_list)
        print(f"Sorted: {new}\n")

if __name__ == "__main__":
    main()