def main(h, w, s):
    """
    >>> main(1, 1, ['#'])
    0 0
    >>> main(3, 3,[
    ...     '.#.',
    ...     '...',
    ...     '...',
    ... ])
    0 1
    """

    for y, s_y in enumerate(s):

        if '#' in s_y:
            print(y, s_y.index('#'))

        else:
            continue


if __name__ == '__main__':
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    main(h, w, s)
