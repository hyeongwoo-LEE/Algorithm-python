n = int(input())

word_set = set()

for _ in range(n):
  word_set.add(input())

word_list = []
for word in word_set:
  word_list.append((word,len(word)))

word_list=sorted(word_list, key=lambda x:(x[1],x[0]))

for word in word_list:
  print(word[0])