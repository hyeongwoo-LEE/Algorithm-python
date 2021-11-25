from itertools import combinations

vowels = ('a','e','i','o','u')

l,c = map(int, input().split())
array = input().split(' ')
array.sort()


for password in list(combinations(array,l)):
  for i in password:
    count = 0
    if i in vowels:
      count += 1
    if(count >= 1 and count + 2 <= l):
      print(''.join(password))