t = int(input())

def bs(target, data):
  start = 0
  end = len(data)-1
  index = -1
  while start <= end:
    mid = (start+end)//2
    if target == data[mid]:
      if index != 1:
        index = mid-1
      return index

    elif target < data[mid]:
      end = mid-1
    else:
      start = mid+1
      index = mid
  return index

for _ in range(t):
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  b.sort()
  count = 0
  for i in a:
    count += bs(i,b) + 1
  print(count)