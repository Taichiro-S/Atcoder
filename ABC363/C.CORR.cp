#include <iostream>
#include <string>
#include <set>
#include <algorithm>

int main() {
    int N, K;
    std::cin >> N >> K;
    std::string S;
    std::cin >> S;
    
    std::set<std::string> st;
    std::sort(S.begin(), S.end());
    do {
        st.insert(S);
    } while (std::next_permutation(S.begin(), S.end()));

    int cnt = 0;

    for (const auto& s : st) {
        for (int i = 0; i <= N - K; ++i) {
            std::string sub = s.substr(i, K);
            if (sub == std::string(sub.rbegin(), sub.rend())) {
                ++cnt;
                break;
            }
        }
    }

    std::cout << st.size() - cnt << std::endl;

    return 0;
}
