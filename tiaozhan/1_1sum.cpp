#include <bits/stdc++.h>
using namespace std;
int n=4;
int a[]={1,2,4,7};
int k=13;
bool dfs(int i,int sum){
    //若前n项都经过了计算，并且sum与k相等则返回true
    if(i==n){
        return sum==k;
    }
    if(dfs(i+1,sum)){
        return true;
    }
    if(dfs(i+1,sum+a[i])){
        return true;
    }
    return false;
}
int main(){
    if(dfs(0,0)){
        printf("Yes\n");
    } else {
        printf("No\n");
    }

}