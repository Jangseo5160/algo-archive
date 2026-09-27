#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    int conv_cnt=0;
    int zero_cnt=0;
    while(s!="1"){
        int size=0;
        for(auto a: s){
            if(a=='1')
                size++;
        }
        zero_cnt+=(s.size()-size);
        s.clear();
        conv_cnt++;

        stack<int> stk;
        while(size>0){
            stk.push(size%2);
            size/=2;
        }
        while(!stk.empty()){
            s+=to_string(stk.top());
            stk.pop();
        }
    }
    answer={conv_cnt, zero_cnt};
    return answer;
}