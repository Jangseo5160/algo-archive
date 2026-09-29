#include <string>
#include <vector>
#include <set>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    multiset<int> m; // 오름차순 정렬
    for(auto s:operations){
        if(s[0]=='I'){
            s.erase(0, 2);
            m.insert(stoi(s));
        }
        else if(s=="D -1"){
            if(!m.empty())
                m.erase(m.begin());
        }
        else if(s=="D 1"){
            if(!m.empty())
                m.erase(prev(m.end()));

        }
    }
    if(m.empty()) return {0,0};
    answer = {*m.rbegin(), *m.begin()};
    return answer;
}