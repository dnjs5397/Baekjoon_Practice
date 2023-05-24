N, M = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(list(a-b) + list(b-a)))
