#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    int max_idx = max_element(numbers.begin(), numbers.end())-numbers.begin();
    answer += numbers[max_idx];
    cout << max_idx << " " << answer << endl;
    numbers.erase(numbers.begin() + max_idx);
    int second = max_element(numbers.begin(), numbers.end())-numbers.begin();
    answer *= numbers[second];
    return answer;
}