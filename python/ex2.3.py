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

def rn_int(a, b):
    return random.randint(a, b)

def rn_double(a, b):
    return random.uniform(a, b)

def build_new_from_old(prime, bit):
    max_index = 0
    while prime[max_index] < 2 ** (bit // 2):
        max_index += 1

    while True:
        q = prime[rn_int(0, max_index - 1)]
        if 2 ** ((bit // 2) - 1) < q <= 2 ** (bit // 2) - 1:
            break

    while True:
        epsilon = rn_double(0, 1)
        n = int((2 ** (bit - 1) / q) + ((2 ** (bit - 1)) * epsilon / q))
        if n % 2 == 1:
            n += 1

        u = 0
        while True:
            p = (n + u) * q + 1
            if p > 2 ** bit:
                break
            if power_mod(2, p - 1, p) == 1 and power_mod(2, n + u, p) != 1:
                return p
            u += 2

def print_res(res):
    for i in range(len(res)):
        print(str(i + 1) + "\t\t|\t\t" + str(res[i]))

def main():
    prime = primes(500)

    bit = int(input("Введите количество бит (1-18): "))
    if bit <= 0 or bit >= 18:
        print("Error")
        return

    res = []
    while len(res) != 10:
        p = build_new_from_old(prime, bit)
        if p not in res:
            res.append(p)

    print_res(res)

if __name__ == "__main__":
    main()
