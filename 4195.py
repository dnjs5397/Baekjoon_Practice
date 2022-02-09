# Union-Find 알고리즘
# - 원소들의 연결 여부를 확인하는 알고리즘
# Python에서는 dictionary 자료형을 해시처럼 사용할 수 있다

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]
    
def union(x,y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x
        number[x] += number[y]
        
test_case = int(input())

for i in range(test_case):
    parent = dict()
    number = dict()
    
    f = int(input())
    
    for j in range(f):
        x, y= input().split(' ')
        
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
            
        union(x,y)
        
        print(number[find(x)])