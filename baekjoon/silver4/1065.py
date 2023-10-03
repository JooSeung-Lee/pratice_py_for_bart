import sys
input = sys.stdin.readline
N = int(input())

if N < 100:
    print(N)

else:
    cnt = 0
    for i in range(100, N+1):
        i = str(i)
        n0 = int(i[0])
        n1 = int(i[1])
        n2 = int(i[2])
        if n0-n1 == n1-n2:
            cnt+=1
    print(99+cnt)
