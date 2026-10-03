#include <string>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> parent(101);

int isParent(int a){
    if(parent[a]==a) return a;
    return parent[a]=isParent(parent[a]);
}

bool isConnected(int a, int b){
    a=isParent(a);
    b=isParent(b);
    if(a==b) return true;
    parent[b]=a;
    return false;
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    sort(costs.begin(), costs.end(), [](auto& a, auto&b){
        return a[2]<b[2];
    });
    

    for(int i=0; i<n; i++){
        parent[i]=i;
    }
    
    for(auto c:costs){
        int a=c[0];
        int b=c[1];
        int weight = c[2];
        if(isConnected(a, b)) continue;
        answer+=weight;
    }
    return answer;
}