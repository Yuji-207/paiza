def main():

    h, w = map(int, input().split())

    for y in range(h):

        s = input()
        end = w - 1  # 右端の文字のインデックス

        if s[1] == '#':
            print(y, 0)

        _ = [print(y, x) for x in range(1, end) if s[x-1] == s[x+1] == '#']

        if s[end-1] == '#':
            print(y, end)
    

if __name__ == '__main__':
    main()
