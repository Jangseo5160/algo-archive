#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array) {
    vector<int> answer;
    auto idx = max_element(array.begin(), array.end());

    answer.push_back(*idx);
    answer.push_back(idx-array.begin());
    return answer;
}