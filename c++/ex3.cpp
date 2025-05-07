#include <iostream>
#include <cmath>


#define epsilon                0.000001
#define limit                  1000
#define max_denominator        10000

int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

int is_possibly_rational(double x) {
    for (int b = 1; b <= max_denominator; b++) {
        int a = (int)round(x * b);
        if (fabs(x - (double)a / b) < epsilon) {
            int common_divisor = gcd(a, b);
            std::cout << a / common_divisor << "/" <<  b / common_divisor << std::endl;
            return 1;
        }
    }
    return -1;
}

void print(double num){
    if (num == -1){
        std::cout << "infinity" << std::endl;
    }
    else if (is_possibly_rational(num) == 1){
    }
    else{
        std::cout << "irrational"<< std::endl;
    }
}

void input(int& a,int& b){
    std::cin >> a >> b;
}

double summing(int a,int b){
    double cur;
    double sum_past = 0,sum = 0;

    cur = 1./b;
    sum_past = cur;
    sum = cur;

    for (int n = 2;n<limit;n ++){
        cur = pow(n,a)/pow(b,n);
        sum += cur;
        if (fabs(sum-sum_past) < epsilon){
            return sum;
        }
        sum_past = sum;
    }
    return -1;
}

int main(void){
    int a,b;

    input(a,b);

    double res = summing(a,b);

    print(res);
}