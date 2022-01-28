def main():

    n, m, q = map(int, input().split())
    
    ts = [''] * n  # 得意な仕事のリスト
    for i in range(q):
        e, t = input().split()
        e = int(e)
        ts[e-1] += t  # ID-1のインデックスに得意な仕事を追加

    max_eff = 0  # 最大の仕事効率性
    for i in range(n):  # 各日の効率性を計算

        eff = 0  # 仕事効率性
        for j in range(m):
            worker = (i + j) % n  # 仕事を担当する従業員

            if str(j + 1) in ts[worker]:
                eff += 1

        if eff > max_eff:
            max_eff = eff

    print(max_eff)


if __name__ == '__main__':
    main()
