import random
import math

# Глобальный генератор случайных чисел
mt_rand = random.Random()

def primes(n):
    # Решето Эратосфена
    is_prime = [True] * (n + 1)
    primes = []

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)

    return primes

def builder_test(prime, bit):
    # Построение числа n
    max_index = 0 # индекс используемый для выбора простых чисел из prime
    max_pow = 1   # степень до которой мы будем возводить простые числа из prime

    while max_index < len(prime) and prime[max_index] < 2 ** (bit - 1):
        max_index += 1
    while 2 ** max_pow < 2 ** (bit - 1):
        max_pow += 1

    m = 1
    q = []

    while True:
        num = rn(0, max_index - 1)
        power = rn(1, max_pow)

        if pow(prime[num], power) != 0:  # проверка и добавление числа
            if m * pow(prime[num], power) < (2 ** 31 - 1):
                m *= pow(prime[num], power)
                q.append(prime[num])

        if m > 2 ** (bit - 2):  # проверка размера числа
            if m >= 2 ** (bit - 1):
                m = 1
                q.clear()
            else:
                break

    n = 2 * m + 1
    return n, q

def test_millera(n, t, q):
    # Тест Миллера
    a = []  # числа для проверки 1<aj<n
    while len(a) != t:
        aj = rn(2, n - 1)
        if aj not in a:
            a.append(aj)

    for aj in a:  # проверка степени числа
        if power_mod(aj, n - 1, n) != 1:
            return 0

    flag = True
    i = 0
    for aj in a:
        if i < len(q) and power_mod(aj, (n - 1) // q[i], n) != 1:
            flag = False
            i += 1

    if flag:
        return 0

    return 1

def power_mod(a, b, n):
    # Быстрое возведение в степень по модулю
    result = 1
    base = a % n

    while b > 0:
        if b & 1:
            result = (result * base) % n
        base = (base * base) % n
        b >>= 1

    return result

def rn(a, b):
    # Глобальный рандомайзер
    return mt_rand.randint(a, b)

def print_results(res, res_ver_test, otvegnutie):
    # Печать результатов
    print("Prime Numbers\tTest Results\tOccurrences")
    print("----------------------------------------------")
    for i in range(len(res)):
        print(f"{res[i]}\t\t{res_ver_test[i]}\t\t{otvegnutie[i]}")

def main():
    size_primes = 500
    prime = primes(size_primes)

    bit = int(input())
    if bit <= 0 or bit >= 32:
        print("Error")
        exit(1)

    q = []
    res = []
    res_ver_test = []
    otvegnutie = []
    k = 0

    while len(res) != 10:
        n, q = builder_test(prime, bit)
        probability = test_millera(n, 10, q)

        if probability == 1:
            if n not in res:
                res.append(n)

                probability = test_millera(n, 1, q)
                res_ver_test.append("+" if probability == 1 else "-")

                otvegnutie.append(k)
                k = 0
        else:
            k += 1

    print_results(res, res_ver_test, otvegnutie)

if __name__ == "__main__":
    main()
