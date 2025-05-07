#include <iostream>
#include <vector>
#include <tuple>
#include <cmath>
#include <random>
#include <algorithm>

using namespace std;

// Глобальный генератор случайных чисел
mt19937 mt_rand(random_device{}());

vector<int> primes(int n);
pair<int, vector<int>> builder_test(const vector<int>& prime, int bit);
int test_millera(int n, int t, const vector<int>& q);
int power_mod(int a, int b, int n);
int rn(int a, int b);
void print_results(const vector<int>& res, const vector<string>& res_ver_test, const vector<int>& otvegnutie);

int main() {
    int size_primes = 500;
    vector<int> prime = primes(size_primes);

    int bit;
    cin >> bit;
    if(bit<=0 || bit>=32)
    {
        cout<<"Error"<<endl;
        exit(1);
    }
    vector<int> q;
    int n;
    int k = 0;
    int probability;

    vector<int> res;
    vector<string> res_ver_test;
    vector<int> otvegnutie;

    while (res.size() != 10) {
        tie(n, q) = builder_test(prime, bit);
        probability = test_millera(n, 10, q);

        if (probability == 1) {
            if (find(res.begin(), res.end(), n) == res.end()) {
                res.push_back(n);

                probability = test_millera(n, 1, q);
                res_ver_test.push_back(probability == 1 ? "+" : "-");

                otvegnutie.push_back(k);
                k = 0;
            }
        } 
        else {
            k++;
        }
    }

    print_results(res, res_ver_test, otvegnutie);
}

// Решето Эратосфена
vector<int> primes(int n) {
    vector<bool> is_prime(n + 1, true);
    vector<int> primes;

    for (int p = 2; p * p <= n; ++p) {
        if (is_prime[p]) {
            for (int i = p * p; i <= n; i += p)
                is_prime[i] = false;
        }
    }

    for (int p = 2; p <= n; ++p) {
        if (is_prime[p])
            primes.push_back(p);
    }

    return primes;
}

// Построение числа n
pair<int, vector<int>> builder_test(const vector<int>& prime, int bit) {
    int max_index = 0;//индекс используемый для выбора простых чисел из prime
    int max_pow = 1;//степень до которой мы будем возводить простые числа из prime

    while (max_index < prime.size() && prime[max_index] < pow(2, bit - 1)) max_index++;
    while (pow(2, max_pow) < pow(2, bit - 1)) max_pow++;

    int m = 1;
    vector<int> q;

    while (true) {
        int num = rn(0, max_index - 1);
        int power = rn(1, max_pow);

        if (pow(prime[num], power) != 0) { //проверка и добавление числа
            if ((double)m * pow(prime[num], power) < INT32_MAX) {
                m *= pow(prime[num], power);
                q.push_back(prime[num]);
            }
        }

        if (m > pow(2, bit - 2)) {  //проверка размера числа
            if (m >= pow(2, bit - 1)) {
                m = 1;
                q.clear();
            } else {
                break;
            }
        }
    }

    int n = 2 * m + 1;
    return make_pair(n, q);
}

// Тест Миллера
int test_millera(int n, int t, const vector<int>& q) {
    vector<int> a;//числа для проверки 1<aj<n
    while (a.size() != t) {
        int aj = rn(2, n - 1);
        if (find(a.begin(), a.end(), aj) == a.end()) {
            a.push_back(aj);
        }
    }

    for (int aj : a) {    //проверка степени числа
        if (power_mod(aj, n - 1, n) != 1) {
            return 0;
        }
    }

    for (int qi : q) {
        bool flag = true;
        for (int aj : a) {
            if (power_mod(aj, (n - 1) / qi, n) != 1) {
                flag = false;
                break;
            }
        }
        if (flag) {
            return 0; 
        }
    }

    return 1;
}

// Быстрое возведение в степень по модулю
int power_mod(int a, int b, int n) {
    long long result = 1;
    long long base = a % n;

    while (b > 0) {
        if (b & 1) result = (result * base) % n;
        base = (base * base) % n;
        b >>= 1;
    }
    return static_cast<int>(result);
}

// Глобальный рандомайзер
int rn(int a, int b) {
    return uniform_int_distribution<int>(a, b)(mt_rand);
}

// Печать результатов
void print_results(const vector<int>& res, const vector<string>& res_ver_test, const vector<int>& otvegnutie) {
    cout << "Prime Numbers\tTest Results\tOccurrences" << endl;
    cout << "----------------------------------------------" << endl;

    for (size_t i = 0; i < res.size(); ++i) {
        cout << res[i] << "\t\t" << res_ver_test[i] << "\t\t" << otvegnutie[i] << endl;
    }
}
