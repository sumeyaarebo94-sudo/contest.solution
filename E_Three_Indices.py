t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = [-1] * n
    r = [-1] * n
    x = 0
    for i in range(1, n):
        if a[i - 1] < a[x]:
            x = i - 1
        l[i] = x
    x = n - 1
    for i in range(n - 2, -1, -1):
        if a[i + 1] < a[x]:
            x = i + 1
        r[i] = x
    ok = False
    for i in range(1, n - 1):
        if a[l[i]] < a[i] and a[r[i]] < a[i]:
            print("YES")
            print(l[i] + 1, i + 1, r[i] + 1)
            ok = True
            break
    if not ok:
        print("NO")