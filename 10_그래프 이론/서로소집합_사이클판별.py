
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):

    parent_a = find_parent(parent,a)
    parent_b = find_parent(parent,b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


v,e = map(int,input().split())

parent = [i for i in range(v+1)]

cycle = False
for _ in range(e):
    a,b = map(int,input().split())

    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a == parent_b:
        cycle = True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")