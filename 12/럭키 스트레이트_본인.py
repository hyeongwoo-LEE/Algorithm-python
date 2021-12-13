n = input()

length = len(n) // 2

left = 0
right = 0

count = 1
for i in n:
  if count <= length:
    left += int(i)
    count += 1
  else:
    right += int(i)
    count += 1

else:
  if left == right:
    print("LUCKY")
  else:
    print("READY")