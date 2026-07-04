t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        b = a[:]
        b[i] += 1

        product = 1
        for x in b:
            product *= x

        ans = max(ans, product)

    print(ans)