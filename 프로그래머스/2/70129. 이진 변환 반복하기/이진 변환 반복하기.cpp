#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    int convert_cnt = 0;
    int zero_cnt = 0;
    while(s!="1"){
        int temp_zero_cnt = 0;
        for(char c: s){
            if(c=='0'){
                temp_zero_cnt+=1;
            }
        }
        zero_cnt+=temp_zero_cnt;
        convert_cnt+=1;
        int n=s.size()-temp_zero_cnt;
        string result = "";
        while (n>0){
            result = to_string(n%2) + result;
            n/=2;
        }   
        s=result;
    }
    answer.push_back(convert_cnt);
    answer.push_back(zero_cnt);
    return answer;
}