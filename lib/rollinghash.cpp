
const int MOD_NUM = 2;
// base : 9973
class RollingHash {
    vector<LL> hash[MOD_NUM];
    vector<LL> mod = {999999937LL, 1000000007LL};
    LL base = 9973;

   public:
    RollingHash(string s) { initialize(s); }

    vector<LL> getHashNum(int left, int right) {
        vector<LL> res(MOD_NUM);
        for (int i = 0; i < MOD_NUM; i++) {
            res[i] =
                ((hash[i][right] -
                  hash[i][left] * this->mpower(base, right - left, mod[i])) %
                     mod[i] +
                 mod[i]) %
                mod[i];
        }

        return res;
    }

   private:
    void initialize(string s) {
        for (int i = 0; i < MOD_NUM; i++) {
            hash[i].assign(s.size() + 1, 0);
            for (int j = 0; j < s.size(); j++) {
                hash[i][j + 1] = (hash[i][j] * base + s[j]) % mod[i];
            }
        }
    }

    LL mpower(LL x, LL n, LL mod) {
        if (n == 0) {
            return 1;
        } else if (n % 2 == 0) {
            return mpower(x * x % mod, n / 2, mod);
        } else {
            return x * mpower(x, n - 1, mod) % mod;
        }
    }
};
