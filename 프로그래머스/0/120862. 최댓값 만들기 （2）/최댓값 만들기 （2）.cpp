#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    vector<int> plus;
    vector<int> minus;
    for (auto n:numbers){
        if (n>=0) plus.push_back(n);
        else minus.push_back(n);
    }
    sort(plus.rbegin(), plus.rend());
    sort(minus.begin(), minus.end());
    if(minus.size()>=2 && plus.size()>=2){
        int temp1 = minus[0]*minus[1];
        int temp2 = plus[0]*plus[1];
        if (temp1>temp2) return temp1;
        else return temp2;
    }
    else if (minus.size()>=2){
        return minus[0]*minus[1];
    }
    else if (plus.size()>=2){
        return plus[0]*plus[1];
    }
    else return plus[0] * minus[0];
    return answer;
}