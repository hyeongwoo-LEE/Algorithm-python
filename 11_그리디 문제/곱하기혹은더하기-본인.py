n = input()

result = 0
for i in range(len(n)):
  num = int(n[i])
  if result == 0 or result == 1: #생각 못한 케이스 result 가 1일 경우에도 + 연산을 수행해야한다.
    result += num
  else:
    if num == 0 or num == 1:
      result += num # 결국 더하기 연산 이므로 위의 if 절과 합치는 것이 바람직
    else:
      result *= num

print(result)