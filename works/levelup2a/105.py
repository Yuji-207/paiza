def main(h, w, s):
    """
    >>> main(1, 1, ['.'])
    0 0
    >>> main(2, 2, [
    ...     '#.',
    ...     '.#'
    ... ])
    0 1
    1 0
    >>> main(3, 3, [
    ...     '##.',
    ...     '###',
    ...     '...'
    ... ])
    0 0
    0 2
    >>> main(10, 10, [
    ...     '##########',
    ...     '..........',
    ...     '##########',
    ...     '##########',
    ...     '..........',
    ...     '#.#.#.#.#.',
    ...     '.#.#.#.#.#',
    ...     '#.#.#.#.#.',
    ...     '.#.#.#.#.#',
    ...     '..........'
    ... ])
    6 0
    6 2
    6 4
    6 6
    6 8
    7 1
    7 3
    7 5
    7 7
    7 9
    """

    y_end = w - 1  # 右端のインデックス
    x_end = h - 1  # 下端のインデックス

    for y in range(h):
        for x in range(w):
            
            if x == 0 or s[y][x-1] == '#':
                if x == x_end or s[y][x+1] == '#':
                    if y == 0 or s[y-1][x] == '#':
                        if y == y_end or s[y+1][x] == '#':

                            print(y, x)


if __name__ == '__main__':
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    main(h, w, s)