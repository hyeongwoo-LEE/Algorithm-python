n,m = map(int,input().split())
parent = [i for i in range(n+1)]

#부모 노드 찾기
def find_parent(parent,x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

#집합 합치기
def union_parent(parent,a,b):
  parent_a =find_parent(parent,a)
  parent_b =find_parent(parent,b)

  if parent_a < parent_b:
    parent[parent_b] = parent_a
  else:
    parent[parent_a] = parent_b

edges = []
for _ in range(m):
  a,b,c = map(int,input().split())
  edges.append((c,a,b))

edges.sort()

result = 0
max_cost = 0
for edge in edges:
  c,a,b = edge
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result += c
    max_cost = c

print(result-max_cost)