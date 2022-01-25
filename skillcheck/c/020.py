def main():
    
    m, p, q = map(int, input().split())
    
    remain = m * (1 - p / 100)
    remain = remain * (1 - q / 100)
    print(remain)
    
    
if __name__ == '__main__':
    main()
