#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    // 인덱스 방식
    for(auto i=0; i<numbers.size(); i++){
        answer.push_back(numbers[i]*2);
    }
    
    // // ranged 방식
    // for (auto n:numbers){
    //     answer.push_back(n*2);
    // }
    // // ranged 원본 수정 방식
    // for (auto& n: numbers){
    //     n*=2;
    // }
    return answer;
}