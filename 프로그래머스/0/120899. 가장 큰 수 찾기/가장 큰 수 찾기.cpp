#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array) {
    vector<int> answer;
    int idx = max_element(array.begin(), array.end())-array.begin();
    int num = *max_element(array.begin(), array.end());
    answer.push_back(num);
    answer.push_back(idx);
    return answer;
}