n, m = [int(i) for i in input().split()]
spiral = [[0] * m for _ in range(n)]
c = 1
    for j in range(m - k - 2, k - 1, -1):  
        if spiral[n - k - 1][j] == 0:
            spiral[n - k - 1][j] = c 
            c += 1
    for i in range(n - k - 2, k, -1):  
        if spiral[i][k] == 0:
            spiral[i][k] = c 
            c += 1
for i in range(n):  
    for j in range(m):
        print(str(spiral[i][j]).ljust(3), end=' ')
    print()
