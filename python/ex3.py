import math

epsilon = 0.000001
limit = 1000
max_denominator = 10000

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_possibly_rational(x):
    for b in range(1, max_denominator + 1):
        a = round(x * b)
        if abs(x - a / b) < epsilon:
            common_divisor = gcd(a, b)
            print(f"{a // common_divisor}/{b // common_divisor}")
            return 1
    return -1

def print_result(num):
    if num == -1:
        print("infinity")
    elif is_possibly_rational(num) == 1:
        pass
    else:
        print("irrational")

def input_values():
    a, b = map(int, input().split())
    return a, b

def summing(a, b):
    cur = 1 / b
    sum_past = cur
    sum_value = cur

    for n in range(2, limit):
        cur = (n ** a) / (b ** n)
        sum_value += cur
        if abs(sum_value - sum_past) < epsilon:
            return sum_value
        sum_past = sum_value
    return -1

def main():
    a, b = input_values()
    res = summing(a, b)
    print_result(res)

if __name__ == "__main__":
    main()
