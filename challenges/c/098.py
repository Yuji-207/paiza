def main():
    
    n = int(input())
    s = [int(input()) for _ in range(n)]
    m = int(input())
    
    for i in range(m):
        
        a, b, x = map(int, input().split())
        
        max_ball = s[a-1]
        x = x if x < max_ball else max_ball  # 実際にパスするボールの数
        
        s[a-1] = max_ball - x
        s[b-1] += x
        
    _ = [print(ball) for ball in s]
        
    
if __name__ == '__main__':
    main()
