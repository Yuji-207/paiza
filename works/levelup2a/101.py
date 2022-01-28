def main():

    h, w, n = map(int, input().split())
    s = [input() for _ in range(h)]

    for _ in range(n):
        y, x = map(int, input().split())
        print(s[y][x])


if __name__ == '__main__':
    main()
