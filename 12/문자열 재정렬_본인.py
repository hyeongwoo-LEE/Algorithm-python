data = input()

alpha = []
num = 0
for i in data:
  if i.isalpha():
    alpha.append(i)
  else:
    num += int(i)

alpha.sort()

for i in alpha:
  print(i,end="")

if num != 0:
    print(num)