def main():
    
    h, w, n = map(int, input().split())
    s = [input() for _ in range(h)]
    
    for _ in range(n):
        
        y, x = map(int, input().split())
        s_y = s[y]
        s[y] = s_y[:x] + '#' + s_y[x+1:]

    _ = [print(s_y) for s_y in s]
        

if __name__ == '__main__':
    main()
