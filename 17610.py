import itertools

a = [1,5,7]
result = []
for i in range(1, len(a)+1):
    tmp = list(itertools.combinations(a, i))
    for val in tmp:
        result.append(sum(val))

print(result)