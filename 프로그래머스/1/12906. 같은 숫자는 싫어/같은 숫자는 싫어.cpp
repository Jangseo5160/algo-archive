#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    for(auto a: arr){
        if(answer.size()==0) answer.push_back(a);
        else{
            if (answer[answer.size()-1] != a){
                answer.push_back(a);
            }
        }
    }

    return answer;
}