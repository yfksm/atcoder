#include <bits/stdc++.h>
using namespace std;
#define REP(i, m, n) for (int i = m; i < n; i++)
#define rep(i, n) REP(i, 0, n)
#define ALL(a) (a).begin(), (a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define dup(x, y) (((x) + (y)-1) / (y))
#define PI 3.14159265359
typedef long long LL;
const LL MOD = 1e9 + 7;
const LL LLINF = 1LL << 60;
const int INF = 1 << 30;

template <class T>
inline void chmax(T &a, T b) {
    if (a < b) {
        a = b;
    }
}
template <class T>
inline void chmin(T &a, T b) {
    if (a > b) {
        a = b;
    }
}
template <class T>
inline T lcm(T x, T y) {
    return x / __gcd(x, y) * y;
}
template <class T>
inline void print_vector(vector<T> vec) {
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
    cout << endl;
}
template <class T>
inline T mpower(T x, T n) {
    if (n == 0) {
        return 1;
    } else if (n % 2 == 0) {
        return mpower(x * x % MOD, n / 2);
    } else {
        return x * mpower(x, n - 1) % MOD;
    }
}

template <class T>
inline T q_power(T x, T n) {
    if (n == 0) {
        return 1;
    } else if (n % 2 == 0) {
        return q_power(x * x, n / 2);
    } else {
        return x * q_power(x, n - 1);
    }
}

LL mfrac(LL x) {
    LL res = 1;
    for (LL i = x; i >= 1; i--) {
        res *= i;
        res %= MOD;
    }
    return res;
}

int main(void) {

    return 0;
}
