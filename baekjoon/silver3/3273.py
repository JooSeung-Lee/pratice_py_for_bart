import sys

input = sys.stdin.readline

n = int(input())
seq_list = list(map(int, input().split())) # [1, 2, 3] 만듦
x = int(input()) # target

sort_list = sorted(seq_list)

left = 0
right = n-1
cnt = 0

while True:
    if left >= right:
        break

    sum = sort_list[left] + sort_list[right]

    if sum == x:
        cnt+=1
        left+=1
        right-=1

    elif sum < x:
        left+=1
    
    else:
        right-=1

print(cnt)
