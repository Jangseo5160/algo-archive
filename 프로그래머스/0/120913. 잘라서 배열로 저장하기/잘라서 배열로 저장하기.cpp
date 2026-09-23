#include <string>
#include <vector>

using namespace std;

vector<string> solution(string my_str, int n) {
    vector<string> answer;
    int len = my_str.size();
    for (int i=0; i<len/n; i++){
        string temp = "";
        for (int j=i*n; j<(i+1)*n; j++){
            temp+=my_str[j];
        }
        answer.push_back(temp);
    }
    string temp = "";
    if(len%n!=0){
        for (int i=(len/n)*n; i<len; i++){
            temp+=my_str[i];
        }
    answer.push_back(temp);
    }
    return answer;
}