#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> array, int n) {
    int answer = 0;
    sort(array.begin(), array.end());
    vector<int> temp = array;
    for(auto& a:temp){
        a-=n;
        if(a<0) a*=-1;
    }
    auto p = min_element(temp.begin(), temp.end()) - temp.begin();
    answer = array[p];
    return answer;
}