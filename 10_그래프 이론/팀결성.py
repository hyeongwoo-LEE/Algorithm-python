n, m = map(int, input().split())


# 부모노드 find
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 집합 합치기 union
def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


parent = [i for i in range(n + 1)]

for _ in range(m):
    command, a, b = map(int, input().split())

    if command == 1:
        parent_a = find_parent(parent, a)
        parent_b = find_parent(parent, b)
        if parent_a == parent_b:
            print("YES")
        else:
            print("NO")
    else:
        union_parent(parent, a, b)