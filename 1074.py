def solve(n,x,y):
    global result
    if x == X and y == Y:
        print(int(result))
        exit(0)
        
    if not (x <= X < x+n and y <= Y < y+n):
        result += n*n
        return 
    
    solve(n / 2, x, y)
    solve(n / 2, x, y + n / 2)
    solve(n / 2, x + n / 2, y)
    solve(n / 2, x + n / 2, y + n / 2)
    
result = 0
N, X, Y = map(int,input().split(' '))
solve(2 ** N, 0, 0)