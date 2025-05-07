def who_wins(n, m, nums):
    # dp[i] — это максимальная разница очков (Павел - Вика),
    dp = [float('-inf')] * (n + 1)
    dp[n] = 0  # если все числа уже удалены, разница очков = 0

    # от "всё удалено" к "всё ещё осталось"
    for i in range(n - 1, -1, -1):
        current_sum = 0  # сумма чисел, которые мы возьмём на этом шаге

        # Пробуем взять от 1 до m чисел если они остались
        for k in range(1, m + 1):
            if i + k <= n:
                current_sum += nums[i + k - 1]

                # dp[i + k] — это разница очков, которую получит соперник после нас
                # Т.е. забирает current_sum, потом соперник играет с позиции i + k
                dp[i] = max(dp[i], current_sum - dp[i + k])

    return 1 if dp[0] > 0 else 0

def IO():
    n, m = map(int, input("Input n m: ").split())
    if not (5 <= n <= 50000) or not (4 <= m <= 100):
        print("Error")
        exit(1)
    nums = list(map(int, input("Input numbers: ").split()))
    print(who_wins(n, m, nums))

def main():
    IO()

if __name__ == "__main__":
    main()
