#include <string>
#include <vector>
#include<algorithm>

using namespace std;
vector<int> parent(101);


int find(int a){
    if(parent[a]==a) return a;
    return parent[a]=find(parent[a]);
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    sort(costs.begin(), costs.end(), [](auto& a, auto& b){
        return a[2]<b[2];
    });
    
    for(int i=0; i<n; i++){
        parent[i]=i;
    }
    
    for(auto c:costs){
        int a=c[0];
        int b=c[1];
        int weight=c[2];
        a=find(a);
        b=find(b);
        if(a!=b){
            answer+=weight;
            parent[b]=a;
        }
        
    }
        
    
    
    return answer;
}