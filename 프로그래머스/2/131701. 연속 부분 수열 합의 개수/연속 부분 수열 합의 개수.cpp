#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<int> elements) {
    int answer = 0;
    unordered_map<int, int> m;
    for(int start=0; start<elements.size(); start++){
        int temp = 0;
        for(int length=1; length<=elements.size(); length++){
            temp+=elements[(start+length)%elements.size()];
            m[temp]++;
        }
    }
    answer = m.size();
    return answer;
}