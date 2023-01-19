n = int(input())
sang = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))

sang.sort()

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end)//2
    if array[mid] == target:
      return True
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1

  return False


for i in range(m):
  if binary_search(sang, num[i], 0, n-1):
    print(1,end=' ')
  else:
    print(0,end=' ')