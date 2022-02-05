import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int,input().split()))

def bs(target, start, end):
  while start <= end:
    mid = (start+end)//2
    if answer[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return start

answer = [0]

for i in data:
  if answer[-1] < i:
    answer.append(i)
  else:
    answer[bs(i,0,len(answer)-1)] = i
print(len(data)-(len(answer)-1))