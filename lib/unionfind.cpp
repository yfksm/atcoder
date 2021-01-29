
class UnionFind {
   public:
    // rank:それぞれの木の深さ
    vector<int> rank;
    // p:ポインタ的な配列
    vector<int> p;
    UnionFind() {}
    UnionFind(int size) {
        rank.resize(size, 0);
        p.resize(size, 0);

        //最初は、全ての値は別の木に属するようにする
        //{0},{1},{2},...といった数字一つのみを持つ木が作られる
        for (int i = 0; i < size; i++) {
            makeSet(i);
        }
    };

    // ただ一つの要素xを持つ木を作成する
    void makeSet(int x) {
        p[x] = x;
        rank[x] = 0;
    }

    // 要素xが属する木のルートノードの値を求める
    int findSet(int x) {
        // xがルートノードでないならポインタがさしている先を再帰的に探索する
        //ルートノードならreturnする
        if (x != p[x]) {
            //ここで最終的に返ってくるのはルートノードの値であるため、探索中に経由したすべてのノードのポインタはルートノードへとつながる。
            p[x] = findSet(p[x]);
        }
        return p[x];
    }

    // xとyが同じ木に属しているか判定する
    bool isSame(int x, int y) { return findSet(x) == findSet(y); }

    // xを要素に持つ木とyを要素に持つ木を統合する
    void unite(int x, int y) { link(findSet(x), findSet(y)); }

   private:
    // xを根に持つ木とyを根に持つ木を統合する
    void link(int x, int y) {
        //なるべく木が深くならないように、rankが小さい方をrankが大きい方へ統合する
        if (rank[x] > rank[y]) {
            p[y] = x;
        } else {
            p[x] = y;
            //木の深さが同じだったらどうしても一段深くなってしまう
            if (rank[x] == rank[y]) {
                rank[y]++;
            }
        }
    }
};
