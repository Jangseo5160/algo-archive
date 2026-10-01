#include <string>
#include <vector>

using namespace std;

int solution(vector<int> money) {
    int answer = 0;
    vector<int> dp_a(money.size());
    vector<int> dp_b(money.size());
    dp_a[0]=money[0];
    dp_a[1]=max(money[0], money[1]);
    for(int i=2; i<money.size()-1; i++){
        dp_a[i]=max(dp_a[i-1], dp_a[i-2]+money[i]);
    }
    dp_b[0]=0;
    dp_b[1]=money[1];
    for(int i=2; i<money.size(); i++){
        dp_b[i]=max(dp_b[i-1], dp_b[i-2]+money[i]);
    }
    
    answer=max(dp_b[money.size()-1], dp_a[money.size()-2]);
    return answer;
}