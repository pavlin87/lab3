#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int whoWins(int n, int m, const vector<int>& nums) {
    // dp[i] — это максимальная разница очков (Павел - Вика),
    vector<int> dp(n + 1, INT_MIN); 
    dp[n] = 0; // если все числа уже удалены то разница очков  0

    //от "всё удалено" к "всё ещё осталось"
    for (int i = n - 1; i >= 0; --i) {
        int current_sum = 0; 

        for (int k = 1; k <= m && i + k <= n; ++k) {
            current_sum += nums[i + k - 1];

            dp[i] = max(dp[i], current_sum - dp[i + k]);
        }
    }

    return dp[0] > 0 ? 1 : 0;
}

void IO() {
    int n, m;
    cout << "Input n m :\n";
    cin >> n >> m;
    if(n<5 || n>50000 || m<4 || m>100)
    {
        cout<<"Error"<<endl;
        exit(1);
    }
    vector<int> nums(n);
    cout << "Input numbers:\n";
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    cout << whoWins(n, m, nums) << endl;
}

int main() {
    IO();
    return 0;
}
