s = input()
data = []
for i in range(len(s)):
  data.append(s[i:len(s)])

data.sort()

for i in data:
  print(i)