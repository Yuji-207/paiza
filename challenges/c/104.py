def main():
    
    a, b = map(int, input().split())

    answer = False  # 答えの有無

    for i in range(1, 10):  # あ
        for j in range(10):  # い

            if (i * 10 + j) * j == a * 100 + i * 10 + b:
                print(i, j)
                answer = True
                break

        if answer:
            break

    if not answer:
        print('No')


if __name__ == '__main__':
    main()
