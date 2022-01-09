
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent ,parent[x])
    return parent[x]


def union_parent(parent ,a ,b):
    parent_a = find_parent(parent ,a)
    parent_b = find_parent(parent ,b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

v ,e = map(int ,input().split())

parent = [i for i in range( v +1)]
edges = []

for _ in range(e):
    a ,b ,cost = map(int ,input().split())
    edges.append((cost ,a ,b))

edges.sort()

result = 0
for edge in edges:
    cost ,a ,b = edge
    if find_parent(parent ,a) != find_parent(parent ,b):
        union_parent(parent ,a ,b)
        result += cost

print(result)