
# 부모 노드 찾기 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두원소가 속한 집합 합치기 - 합집합 함수
def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

v, e = map(int,input().split())

#부모 테이블 - 자기 자신을 부모로 초기화
parent = [i for i in range(v+1)]

#union 연산 수행
for _ in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

print()

print("부모 테이블: ", end='')
for i in range(1,v+1):
    print(parent[i],end=' ')




