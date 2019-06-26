#include <bits/stdc++.h>
using namespace std;
const int MAX_N=10000;
const int MAX_M=10000;
const int INF=0x3f3f3f3f;
typedef pair<int,int> P;
char maze[MAX_N][MAX_M];
int N,M;
int sx,sy;
int gx,gy;
int d[MAX_N][MAX_M];
int dx[4]={1,0,-1,0},dy[4]={0,1,0,-1};//四个方向
int bfs(){
    queue<P> que;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            d[i][j]=INF;
        }
    }
    que.push(P(sx,sy));
    d[sx][sy]=0;
    while(que.size()){
        P p=que.front();
        que.pop();
        if(p.first==gx&&p.second==gy){
            return d[p.first][p.second];
            //break;
        }
        for(int i=0;i<4;i++){
            int nx=p.first+dx[i],ny=p.second+dy[i];
            if(0<=nx&&nx<N && 0<=ny&&ny<M &&maze[nx][ny]!='*'&&d[nx][ny]==INF){
                P tmp;
                tmp.first=nx;
                tmp.second=ny;
                que.push(tmp);
                d[nx][ny]=d[p.first][p.second]+1;
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