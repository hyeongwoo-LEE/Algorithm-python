n = int(input())

data = []
answer = []
for _ in range(n):
    data.append(list(map(int,input().split())))

def dfs(now_deep,now_index, sum):
    if now_deep == n-1:
        return answer.append(sum)

    left = now_index
    right = now_index + 1

    left_sum = sum + data[now_deep+1][left]
    right_sum = sum + data[now_deep+1][right]

    dfs(now_deep+1,left,left_sum)
    dfs(now_deep+1,right,right_sum)

dfs(0,0,data[0][0])

print(max(answer))
