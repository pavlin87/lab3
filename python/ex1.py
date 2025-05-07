import math

X_START = -3
X_FINITE = 7

def Input():
    X0 = float(input("Input X0: "))
    X1 = float(input("Input X1: "))
    dx = float(input("Input dx: "))
    return X0, X1, dx

def func(x):
    if x >= -3 and x <= -1:
        return -x - 1
    if x > -1 and x <= 1:
        return 0
    if x > 1 and x <= 5:
        return math.sqrt(4 - ((x - 3) * (x - 3)))
    if x > 5 and x <= 7:
        return -x / 2 + 2.5
    return 0

def Output(X0, X1, dx):
    print("x\t\ty\n")
    x = X0
    while x <= X1:
        print(f"{x}\t\t{func(x)}")
        x += dx

def main():
    X0, X1, dx = Input()
    if dx <= 0 or X0 < X_START or X1 > X_FINITE:
        print("Error")
        exit(1)
    Output(X0, X1, dx)

if __name__ == "__main__":
    main()
