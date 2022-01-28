def main():
    """
    >>> main(8, 3, 5)
    4
    >>> main(10, 2, 4)
    5
    >>> main(15, 4, 6)
    8
    >>> main(7, 3, 5)
    3
    >>> main(10, 3, 8)
    5
    >>> main(13, 5, 7)
    8
    >>> main(200000, 1, 5)
    0
    >>> main(1, 1, 2)
    0
    >>> main(3, 5, 6)
    2
    >>> main(8, 2, 4)
    4
    """

    n = int(input())
    a, b = map(int, input().split())
    
    steps = [True] + [False] * n  # 0段目を含めた階段のリスト
    count = 0  # 踏まない段の数
    
    for i in range(n):

        if steps[i]:

            next_a = i + a  # a段上がる
            if next_a < n:
                steps[next_a] = True

                next_b = i + b  # b段上がる
                if next_b < n:
                    steps[next_b] = True

        else:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
