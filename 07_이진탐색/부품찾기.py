n = int(input())
exist = list(map(int,input().split()))
m = int(input())
want = list(map(int,input().split()))

def binary_search(array,target,start,end):
  while start <= end:
    mid = (start+end)//2

    if array[mid] == target:
      return mid

    elif array[mid] < mid:
      end = mid-1

    else:
      start = mid+1

  return None

for i in range(len(want)):
  if binary_search(exist,want[i],0,n-1) != None:
    print("yes", end=' ')
  else:
    print("no", end=' ')