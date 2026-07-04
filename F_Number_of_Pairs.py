from bisect import bisect_left, bisect_right

t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    a = sorted(map(int, input().split()))

    ans = 0
    for i in range(n):
        x = bisect_left(a, l - a[i], i + 1)
        y = bisect_right(a, r - a[i], i + 1)
        ans += y - x

    print(ans)