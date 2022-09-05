#include <bits/stdc++.h>
#include <vector>

using namespace std;

int returnRank(vector<int> &ranked, int score) {
    int prevRanked = -1;
    int currentRank = 0;
    for (int i = 0; i < ranked.size(); i++) {
        if (prevRanked != ranked[i]) {
            currentRank++;
        }
        if (score >= ranked[i]) {
            return currentRank;
        }
        prevRanked = ranked[i];
    }
    return currentRank + 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    vector<int> ranked;
    int m;
    vector<int> player;
    vector<int> results;

    cin >> n;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        ranked.push_back(t);
    }

    cin >> m;
    for (int i = 0; i < m; i++) {
        int t;
        cin >> t;
        player.push_back(t);
    }

    for (int i = 0; i < m; i++) {
        int t = returnRank(ranked, player[i]);
        results.push_back(t);
    }

    for (int i = 0; i < results.size(); i++) {
        cout << results[i] << '\n';
    }

    return 0;
}