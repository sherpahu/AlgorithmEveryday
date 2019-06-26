#include <bits/stdc++.h>
using namespace std;
int N,M;
int sx,sy,gx,gy;
const int MAX_N=1000,MAX_M=1000;
const int INF=0x3f3f3f3f;
const int dx[]={1,0,-1,0},dy[]={0,1,0,-1};
int maze[MAX_N][MAX_M];
int d[MAX_N][MAX_M];
int flag[MAX_N][MAX_M]={0};
typedef pair<int,int> P;
int bfs(){
    queue<P> que;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            d[i][j]=INF;
        }
    }
    d[sx][sy]=0;
    que.push(P(sx,sy));
    while (que.size()){
        P p=que.front();
        que.pop();
        if(p.first==gx&&p.second==gy){
            return d[gx][gy];
        }
        for(int i=0;i<4;i++){
            int nx=p.first+dx[i],ny=p.second+dy[i];
            if(0<=nx&&nx<N && 0<=ny&&ny<M && maze[nx][ny]!='*' && flag[nx][ny]!=1){
                d[nx][ny]=d[p.first][p.second]+1;
                que.push(P(nx,ny));
                flag[nx][ny]=1;
                printf("here");
            }
        }
    }
    return -1;
}
int main(){
    // N=10;
    // M=10;
    // sx=1;
    // sy=0;
    // gx=8;
    // gy=9;
    scanf("%d%d",&N,&M);
    for(int i=0;i<N;i++){
        scanf("%s",maze[i]);
    }
    scanf("%d%d%d%d",&sx,&sy,&gx,&gy);
    int rst=bfs();
    printf("%d\n",rst);
}