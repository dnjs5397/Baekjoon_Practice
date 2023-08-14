S = input()
T = input()

s = [i for i in S]
t = [i for i in T]


def word(arr):
    if arr == []:
        return

    if arr == s:
        print(1)
        exit(0)

    if arr[-1] == 'A':
        word(arr[:-1])

    if arr[0] == 'B':
        word((list(reversed(arr)))[:-1])


word(t)
print(0)
