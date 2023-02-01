n = int(input())
m = int(input())

VIP = []
for _ in range(m):
  VIP.append(int(input()))

dp = [0] * (n+1)

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
  dp[i] = dp[i-1] + dp[i-2]

pre = 0
answer = 1
for i in range(m):
  answer *= dp[VIP[i]-pre-1]
  pre = VIP[i]

answer *= dp[n-pre]

print(answer)