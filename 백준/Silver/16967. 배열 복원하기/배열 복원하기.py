H, W, X, Y = map(int, input().split())

arr = []
for _ in range(H+X):
    arr.append(list(map(int, input().split())))

for i in range(H+X):
    for j in range(W+Y):
        tx = i + X
        ty = j + Y
        if 0 <= tx < H+X and 0 <= ty < W+Y:
            arr[tx][ty] -= arr[i][j]

for i in range(H):
    for j in range(W):
        print(arr[i][j], end=' ')
    print()
