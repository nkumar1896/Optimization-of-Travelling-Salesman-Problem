#include<stdio.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#include<limits.h>
#include <utility>
#include <algorithm> 
#include<iostream>
#include <vector>
#include <map>
#include <set>
#include<fstream>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include<stdlib.h>
//#define size 10 
#define min(a,b) a>b?b:a
#define sizePOW 1024
using namespace std;
ofstream GApath;
ofstream SApath; 
ofstream DMpath;
ofstream pathdm; 
ofstream GAdistance;
ofstream SAdistance;
ofstream DMdistance;
ofstream GAtime;
ofstream SAtime;
ofstream DMtime;
ifstream nvalue;
int npow,g[1000][1024],p[1000][1024];
 int originalGraph[100][100];
 int points[10000][2],n;
 int curr_path[10000];
 int new_path[10000];
 int min_path[10000];
 int visited[10000],cost=0;
void get()
{
//printf("No of cities=");
//scanf("%d",&n);
nvalue.open("outtsp.txt");
//scanf("%d",&n);
nvalue>>n;
nvalue.close();
std::fstream fin("matrixtsp.txt");
   // std::vector<std::string> words;
   
    std::string line;
    int i=0,j=0;
    while(fin && getline(fin, line))
    {
        std::string word;
        std::stringstream ss(line);
        
        while(ss && ss >> word)
        {
        	originalGraph[i][j]=atoi(word.c_str());
        	
            std::cout << originalGraph[i][j] << "\t";
            //words.push_back(word);
            j++;
        }
        std::cout << "\n";
        //words.push_back("\n");
        i++,j=0;
    }
}

//dynamic algorithm
int compute(int start,int set)
{	int masked,mask,result=INT_MAX,temp,i;
	if(g[start][set]!=-1)
		return g[start][set];
	for(i=0;i<n;i++)
		{	
			mask=(npow-1)-(1<<i);
			masked=set&mask;
			if(masked!=set)
			{	
				temp=originalGraph[start][i]+compute(i,masked);
				if(temp<result)
					result=temp,p[start][set]=i;
			}
		}
		return g[start][set]=result;
}
void getpath(int start,int set)
{
	if(p[start][set]==-1) return;
	int x=p[start][set];
	int mask=(npow-1)-(1<<x);
	int masked=set&mask;//remove p from set
	printf("%d--> ",x+1);
	pathdm<<"-->"<<x+1;
	DMpath << x+1<<",";
	getpath(x,masked);
	
}
void TSP1()
{	int i,j;

	for(i=0;i<n;i++)
		for(j=0;j<npow;j++) 
				g[i][j]=p[i][j]=-1; 
	for(i=0;i<n;i++)g[i][0]=originalGraph[i][0];
	int result=compute(0,npow-2);//npow-2 to exclude our "home" vertex
//	printf("Tour cost:%d\n",result);
DMdistance << " Minimum Cost: " << result;
	DMdistance.close();
//	printf("Tour path:\n0 ");
	getpath(0,npow-2);
	printf("1\n");
	DMpath << 1;
	DMpath.close();
	pathdm<<"-->"<<1<<"\n";
	pathdm.close();
}


int main()
{
srand(time(NULL));
get();
int r1,r2;
clock_t start_t,end_t, total_t;
clock_t start_t1,end_t1, total_t3;
clock_t start_t2,end_t2, total_t4;

  //Minimum distance using dynamic prog.
 // get();
	start_t1=clock();
	cout<<"\n\nstart time for Dynalic Programming="<<start_t1<<endl;
//	printf("Tour sequence For Dynamic programming=");
//	mincost(0);
DMpath.open("DMpath.txt");
DMtime.open("DMtime.txt");
pathdm.open("pathdm.txt");
DMdistance.open("DMdistance.txt");
DMpath<<1<<",";
   printf("1-->");
  // pathdm<<"DM path:"<<"\n";
   pathdm<<1;
npow=(int)pow(2,n);
//	put();
      TSP1();
	end_t1=clock();
	cout<<"\nend time for Dynalic Programming="<<end_t1<<endl;
	//put();
	double total2 = ((double)(end_t1 - start_t1))/CLOCKS_PER_SEC;
   printf("Total time taken by CPU For Dynamic Programming: %.20f\n", total2  );
   DMtime<<"Time="<<total2;
   DMtime.close();
return 0;
}
