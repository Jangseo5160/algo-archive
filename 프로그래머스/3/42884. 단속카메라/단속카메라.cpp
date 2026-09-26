#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 0;
    int camera = -30001;
    sort(routes.begin(), routes.end(), [](const vector<int>& a,const vector<int>& b){return a[1]<b[1];});
    for(auto v: routes){
        int s=v[0];
        int e=v[1];
        if(camera<s){
            answer++;
            camera = e;
        }
    }
    return answer;
}