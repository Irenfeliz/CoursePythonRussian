n = int(input())
k = int(input())

def josephus(n, k):
    return 0 if n == 0 else (josephus(n - 1, k) + k - 1) % n + 1


print(josephus(n, k))