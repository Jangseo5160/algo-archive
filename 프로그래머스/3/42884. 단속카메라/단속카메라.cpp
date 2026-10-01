#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 0;
    sort(routes.begin(), routes.end(), [](vector<int>a, vector<int>b){return a[1]<b[1];});
    // for(auto c:routes){
    //     cout<<"    "<<c[0] << " "<<c[1];
    // }
    int fin = -30001;
    for(auto c:routes){
        int s=c[0];
        int e=c[1];
        if(fin<s){
            answer++;
            fin=e;
        }
    }
    return answer;
}