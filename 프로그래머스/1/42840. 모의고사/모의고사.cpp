#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer(3);
    vector<int> rule1={1, 2, 3, 4, 5};
    vector<int> rule2={2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> rule3={3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    for(int i=0; i<answers.size(); i++){
        if(answers[i]==rule1[i%5]) answer[0]++;
        if(answers[i]==rule2[i%8]) answer[1]++;
        if(answers[i]==rule3[i%10]) answer[2]++;
    }
    vector<int> final_answer;
    int max_v = *max_element(answer.begin(), answer.end());
    for(int i=0; i<3; i++){
        if(answer[i]==max_v){
            final_answer.push_back(i+1);
        }
    }
    return final_answer;
}