import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0]*N

for i in range(N):
    dp[i] = arr[i]
    #print(dp)
    for j in range(i):
        # 증가하는 부분수열인지 and 현재 비교기준이 (이전까지의 합 + 자신의 합)보다 작을 때
        if arr[j] < arr[i] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]

print(max(dp))
