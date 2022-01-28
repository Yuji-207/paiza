def main():
    """
    >>> main(2, [
    ... [0, 1],
    ... [4, 3]
    ... ])
    2
    >>> main(4, [
    ... [1, 3, 1, 4],
    ... [1, 2, 1, 3],
    ... [2, 1, 3, 4],
    ... [3, 1, 2, 4]
    ... ])
    4
    >>> main(6, [
    ... [3, 9, 0, 1, 5, 3],
    ... [5, 2, 3, 7, 1, 4],
    ... [6, 1, 1, 3, 7, 5],
    ... [6, 5, 2, 1, 1, 6],
    ... [2, 1, 9, 7, 8, 5],
    ... [7, 4, 5, 0, 0, 0]
    ... ])
    4
    """

    n = int(input())
    range_n = range(n)
    max_count = 1  # 最大スワイプ数

    s = []  # 盤面
    for i in range_n:

        s_i = [int(s_j) for s_j in input()]
        s.append(s_i)

        # 盤面の取得と同時に横方向の最大スワイプ数を取得
        max_count = max_swipe(s_i, max_count)

    for s_i in s:  # 消す
        max_count = max_swipe(s_i, max_count)

    # 縦方向の最大スワイプ数を取得
    for s_j in zip(*s):  # 転置
        max_count = max_swipe(s_j, max_count)

    # 右上から左下方向の最大スワイプ数を取得
    for i in range_n:
        s_k = [s[i-j][j] for j in range(i + 1)]  # 左上方向にずれた二次元配列を作成
        max_count = max_swipe(s_k, max_count)

    # 左上から右下方向の最大スワイプ数を取得
    for i in range_n:
        start = n - 1
        s_l = [s[i+j-start][j] for j in range_n[start - i:]]  # 右上方向にずれた二次元配列を作成
        max_count = max_swipe(s_l, max_count)

    print(max_count)


def max_swipe(nums, max_count):
    """
    >>> max_swipe([0, 1], 1)
    2
    >>> max_swipe([9, 8], 1)
    2
    >>> max_swipe([0, 1, 3, 4, 5, 6, 5, 4, 8, 9], 2)
    4
    >>> max_swipe([9, 0, 7, 6, 5, 4, 5, 6, 5, 2], 2)
    4
    >>> max_swipe([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
    10
    >>> max_swipe([0, 3, 1, 4, 2, 5, 3, 6, 4, 7], 1)
    1
    >>> max_swipe([9, 0, 7, 6, 5, 4, 5, 6, 5, 2], 6)
    6
    """

    before = nums[0]  # 左隣（1つ前）の数字
    up_count = 1  # 昇順スワイプ数
    down_count = 1  # 降順スワイプ数

    for num in nums[1:]:

        diff = num - before

        if diff == 1:
            up_count += 1
            down_count = 1
            if up_count > max_count:
                max_count = up_count

        elif diff == -1:
            up_count = 1
            down_count += 1
            if down_count > max_count:
                max_count = down_count

        else:
            up_count = 1
            down_count = 1

        before = num

    return max_count


if __name__ == '__main__':

    main()
