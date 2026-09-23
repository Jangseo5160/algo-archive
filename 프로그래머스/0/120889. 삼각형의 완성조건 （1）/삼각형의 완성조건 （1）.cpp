#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> sides) {
    int answer = 0;
    auto a = max_element(sides.begin(), sides.end());
    int b=0;
    for(auto i = 0; i<3; i++){
        if(i!=a-sides.begin()){
            b+=sides[i];
        }
    }
    if (*a<b) return 1;
    else return 2;
    
    return answer;
}