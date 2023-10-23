n, m = (int(i) for i in input().split())
spiral = []

        x, y = x + dx, y + dy
for i in range(n):
    for j in range(m):
        print(str(spiral[j][i]).ljust(3), end=' ')
    print()
