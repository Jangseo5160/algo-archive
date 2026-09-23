#include <string>
#include <vector>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    for(int i=0; i<my_string.size(); i++){
        if ('1'<=my_string[i] && my_string[i]<='9'){
            string temp="";
            while(i<my_string.size()&&'0'<=my_string[i] && my_string[i]<='9'){
                temp+=my_string[i];
                i++;
            }
            answer+=stoi(temp);
        }
    }
    return answer;
}