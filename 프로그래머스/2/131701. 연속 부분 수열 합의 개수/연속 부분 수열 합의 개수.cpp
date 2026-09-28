#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<int> elements) {
    int answer = 0;
    unordered_map<int, int> m;
    for(int length=1; length<=elements.size(); length++){
        for(int start=0; start<elements.size(); start++){
            int temp=0;
            int k=0;
            while(k<length){
                temp+=elements[(start+k)%elements.size()];
                k++;
            }
            m[temp]++;
        }
    }
    answer = m.size();
    return answer;
}