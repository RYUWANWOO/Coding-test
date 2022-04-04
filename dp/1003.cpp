//
// Created by WanU RYU on 2022/04/05.
//

//
//  main.cpp
//  1003
//
//  Created by WanU RYU on 2022/04/04.
//

#include <iostream>
using namespace std;
int dp[41] = {0};
int main(void){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    for(int i=3;i<41;++i){
        dp[i] = dp[i-1] + dp[i-2];
    }

    int case_num;
    cin >> case_num;

    for(int i=0;i<case_num;++i){
        int num;
        cin >> num;

        if(num == 0){
            cout << 1  << " " << 0 << "\n";
        }else if(num == 1){
            cout << 0 <<" " << 1 << "\n";
        }else{
            cout << dp[num-2] <<" " << dp[num-1] << "\n";
        }

    }

}

