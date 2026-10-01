#include <string>
#include <vector>
#include<algorithm>
#include<iostream>
using namespace std;
vector<int> parent(101);

int findParent(int x){
    if(parent[x]==x)
        return x;
    return parent[x] = findParent(parent[x]);
}

bool unionNode(int a, int b){
    a=findParent(a);
    b=findParent(b);
    if(a==b) return false;
    parent[b]=a;
    return true;
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    sort(costs.begin(), costs.end(), [](const auto& a, const auto& b){return a[2]<b[2];});
    for(int i=0; i<n; i++){
        parent[i]=i;
    }
    
    int cnt=0;
    
    for(const auto& c:costs){
        int a= c[0];
        int b=c[1];
        int cost = c[2];
        if(unionNode(a, b)){
            answer+=cost;
            cnt++;
            if(cnt==n-1)
                break;
        }
    }
    return answer;
}