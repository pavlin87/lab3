import math
import random

def primes(n):
    is_prime = [True] * (n + 1)
    result = []

    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    for p in range(2, n + 1):
        if is_prime[p]:
            result.append(p)

    return result

def power_mod(a, b, n):
    result = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        b //= 2
    return result

def rn(a, b):
    return random.randint(a, b)

def builder_test(prime, bit):
    max_index = 0
    while max_index < len(prime) and prime[max_index] < 2 ** ((bit // 2) + 1):
        max_index += 1

    max_pow = 1
    while 2 ** max_pow < 2 ** ((bit // 2) + 1):
        max_pow += 1

    f = 1
    q = []

    while True:
        num = rn(0, max_index - 1)
        power = rn(1, max_pow)

        p_pow = prime[num] ** power
        if f * p_pow < 2**31:
            f *= p_pow
            q.append(prime[num])

        if f > 2 ** (bit // 2):
            if f >= 2 ** ((bit // 2) + 1):
                f = 1
                q.clear()
            else:
                break

    while True:
        R = rn(2 ** ((bit // 2) - 1) + 1, 2 ** (bit // 2))
        if R % 2 == 0:
            break

    n = R * f + 1
    return n, q

def test_poklin(n, t, q):
    a = []
    while len(a) < t:
        aj = rn(1, n - 1)
        if aj not in a:
            a.append(aj)

    for aj in a:
        if power_mod(aj, n - 1, n) != 1:
            return 0

    for i, aj in enumerate(a):
        if i < len(q) and q[i] != 0:
            if power_mod(aj, (n - 1) // q[i], n) == 1:
                return 0

    return 1

def print_results(res, res_ver_test, otvegnutie):
    print("Prime Numbers\tTest Results\tOccurrences")
    print("----------------------------------------------")
    for n, ver, k in zip(res, res_ver_test, otvegnutie):
        print(f"{n}\t\t{ver}\t\t{k}")

def main():
    size_primes = 500
    prime = primes(size_primes)

    bit = int(input())
    if bit <= 0 or bit >= 32:
        print("error")
        return

    res = []
    res_ver_test = []
    otvegnutie = []
    k = 0

    while len(res) != 10:
        n, q = builder_test(prime, bit)
        probability = test_poklin(n, 10, q)

        if probability == 1 and n not in res:
            res.append(n)
            probability = test_poklin(n, 1, q)
            res_ver_test.append("+" if probability == 1 else "-")
            otvegnutie.append(k)
            k = 0
        else:
            k += 1

    print_results(res, res_ver_test, otvegnutie)

if __name__ == "__main__":
    main()
