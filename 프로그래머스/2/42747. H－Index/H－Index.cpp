#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.rbegin(), citations.rend());
    for(int i=citations[0]; i>=0; i--){
        int over = 0;
        int under=0;
        for(auto a:citations){
            if (a>=i) over++;
            if (a<=i) under++;
        }
        if(over>=i && under<=i) {
            return i;
        }
    }
    return answer;
}