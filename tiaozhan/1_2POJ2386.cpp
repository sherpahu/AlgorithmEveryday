#include <bits/stdc++.h>
using namespace std;
int n=0;
int m=0;
char a[10000][10000];
void dfs(int x,int y){
    a[x][y]='.';
    for(int dx=-1;dx<=1;dx++){
        for(int dy=-1;dy<=1;dy++){
            int nx=x+dx;
            int ny=y+dy;
            if(nx>=0&&nx<n&&ny>=0&&ny<m&&a[nx][ny]=='W'){
                a[nx][ny]='.';
                dfs(nx,ny);
            }
        }
    }
    return;
}
int main(){
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        scanf("%s", a[i]);
    int ans=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(a[i][j]=='W'){
                ans++;
                dfs(i,j);
            }
        }
    }
    printf("%d",ans);
    return 0;
}