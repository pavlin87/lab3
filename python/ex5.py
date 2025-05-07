import math

# Global variables
T = 0.0
Ts = 0.0
r = 0.0
time_limit = 0
aproxCof = (0.0, 0.0)

def korrel(temperatures, mean_y, t):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    mean_x = (time_limit - 1) / 2.0
    for x in range(t + 1):
        sum_xy += (x - mean_x) * (temperatures[x] - mean_y)
        sum_x += (x - mean_x) ** 2
        sum_y += (temperatures[x] - mean_y) ** 2
    return sum_xy / math.sqrt(sum_x * sum_y)

def aprox(x, y):
    n = len(x)
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    for i in range(n):
        sum_xy += x[i] * y[i]
        sum_x += x[i]
        sum_y += y[i]
        sum_x2 += x[i] ** 2
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    b = (sum_y - a * sum_x) / n
    return a, b

def coffee(T, Ts, r, time_limit):
    temperatures = []
    time = []
    temperatures_corr = []

    for t in range(time_limit + 1):
        temperatures.append(Ts + (T - Ts) * math.exp(-r * t))
        time.append(t)

    mean_y = sum(temperatures) / len(temperatures)

    for t in range(time_limit + 1):
        temperatures_corr.append((temperatures[t], korrel(temperatures, mean_y, t)))

    global aproxCof
    aproxCof = aprox(time, temperatures)
    return temperatures_corr

def main():
    global T, Ts, r, time_limit

    T = float(input("T: "))
    Ts = float(input("Ts: "))
    r = float(input("r: "))
    time_limit = int(input("time_limit: "))

    t_c = coffee(T, Ts, r, time_limit)

    print(f"aprox coaf: a = {aproxCof[0]}\tb = {aproxCof[1]}")
    print("Время\tТемпература\t\tКоэф Корреляции")

    for t, (temperature, correlation) in enumerate(t_c):
        print(f"{t}\t{temperature}\t\t{correlation}")

if __name__ == "__main__":
    main()
