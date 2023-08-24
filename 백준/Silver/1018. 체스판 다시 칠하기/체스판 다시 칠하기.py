N, M = map(int, input().split())
arr = [input() for _ in range(N)]
bb = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB",
      "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]

ww = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
      "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]

answer = 214700000

for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        if arr[i][j] == 'B':
            for k in range(8):
                for q in range(8):
                    if arr[i+k][j+q] != bb[k][q]:
                        cnt1 += 1
                    if arr[i+k][j+q] != ww[k][q]:
                        cnt2 += 1
            answer = min(answer, cnt1, cnt2)
        else:
            for k in range(8):
                for q in range(8):
                    if arr[i+k][j+q] != bb[k][q]:
                        cnt1 += 1
                    if arr[i+k][j+q] != ww[k][q]:
                        cnt2 += 1
            answer = min(answer, cnt1, cnt2)

print(answer)