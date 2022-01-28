def main(h, w, s):
    """
    入力が 2 <= h, w <= 20 であるべきでは？
    >>> main(3, 3, [
    ...     '###',
    ...     '...',
    ...     '###'
    ... ])
    1 0
    1 1
    1 2
    >>> main(4, 4, [
    ...     '#.#.',
    ...     '.#.#',
    ...     '.#.#',
    ...     '#.#.'
    ... ])
    0 1
    0 3
    3 1
    3 3
    >>> main(1, 20, [
    ...     '####################'
    ... ])
    20
    >>> main(20, 1, [
    ...     '.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'
    ... ])
    0
    >>> main(1, 1, [
    ...     '.'
    ... ])
    0
    >>> main(1, 1, [
    ...     '#'    
    ... ])
    1
    """
    
    bottom = h - 1  # 下端の文字のインデックス
    range_w = range(w)

    # 1番上の段
    for x in range_w:
        if s[1][x] == '#':
            print(0, x)
    
    # 中央の段
    for y in range(1, bottom):
        _ = [print(y, x) for x in range_w if s[y-1][x] == s[y+1][x] == '#']

    # 1番下の段
    for x in range_w:
        if s[bottom-1][x] == '#':
            print(bottom, x)


if __name__ == '__main__':
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    main(h, w, s)
