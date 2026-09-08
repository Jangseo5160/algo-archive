#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    int convert_cnt = 0;
    int zero_cnt = 0;
    while(s!="1"){
        int one_cnt = 0;
        for(char c: s){
            if(c=='0'){
                zero_cnt++;
            }
            else one_cnt++;
        }
        s = "";
        while (one_cnt>0){
            s = to_string(one_cnt%2) + s;
            one_cnt/=2;
        }   
        convert_cnt+=1;
    }
    return {convert_cnt, zero_cnt}; //vector<int>
}