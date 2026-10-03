#include <string>
#include <vector>

using namespace std;

int solution(vector<int> money) {
    int answer = 0;
    int n=money.size();
    vector<int> dpa(n);
    vector<int> dpb(n);
    
    dpa[0]= money[0];
    dpa[1] = max(money[0], money[1]);
    for(int i=2; i<n-1; i++){
        dpa[i]=max(dpa[i-1], money[i]+dpa[i-2]);
    }
    
    dpb[0]= 0;
    dpb[1] = money[1];
    
    for(int i=2; i<n; i++){
        dpb[i]=max(dpb[i-1], money[i]+dpb[i-2]);
    }
    
    answer= max(dpa[n-2], dpb[n-1]);
    return answer;
}