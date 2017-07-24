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
#include <sstream>
#include <string>
#include <vector>
#include<stdlib.h>
#include<fstream>
//#define size 10 
#define min(a,b) a>b?b:a
#define sizePOW 1024
using namespace std;
ofstream SApath; 
//ofstream DMpath; 
ofstream pathsa;
//ofstream GAdistance;
ofstream SAdistance;
//ofstream DMdistance;
//ofstream GAtime;
ofstream SAtime;
//ofstream DMtime;
ifstream nvalue;
//int npow,g[1000][1024],p[1000][1024];
 int originalGraph[1][2];
 int points[10000][2],n;
 int curr_path[10000];
 int new_path[10000];
 int min_path[10000];
 int visited[10000],cost=0;
int generateRandomNumber()
{
	return (rand()%(n-1))+1;
}
int generateRandomNumber1()
{
	return (rand()%(100-1))+1;
}
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

//simulated annealing
void init()
{
//int	curr_path[n+1];
	curr_path[0]=curr_path[n]=0;
	for(int i=1;i<n;i++)
	{
		curr_path[i]=i;
	}

//int new_path[n+1];
	new_path[0]=new_path[n]=0;
	for(int i=1;i<n;i++)
	{
		new_path[i]=i;
	}
//int	min_path[n+1];
	min_path[0]=new_path[n]=0;
	for(int i=1;i<n;i++)
	{
		min_path[i]=i;
	}
//	print();
	
	
}

void swap(int r1,int r2,int *new_path)
{
	int temp=new_path[r1];
	new_path[r1]=new_path[r2];
	new_path[r2]=temp;
}
void two_opt(int r1,int r2,int *new_path)
{
	int i,j,k,limit,temp;
	if(r1>r2)
	{
		temp=r1;
		r1=r2;
		r2=temp;
	}
	//swap(r1,r2,new_path);
	limit=floor((r2-r1+1)/2);
	i=r1,j=r2;
	for(k=0;k<limit+1;k++)
	{
		swap(i++,j--,new_path);
	}
}
int getCost(int *path)
{
	int cost=0;
	for(int i=0;i<n;i++)
	{
		cost+=originalGraph[path[i]][path[(i+1)%n]];
	}
	return cost;
}
void retraceMinPath(int *min_path)
{
   //cout<<"time="<<total_t<<endl;
  // printf("The shortest cost obtained For SA is=%d\n",getCost(min_path));
   printf("Tour sequence For Simulated Annealing=");
  for(int i=0;i<n;i++)
  {
  
   printf("%d-->",min_path[i]+1);
   
   SApath<<min_path[i]+1<<",";
   pathsa<<min_path[i]+1<<"-->";

  
}
  printf("%d",min_path[0]+1);
  printf("\n");
  SApath<<min_path[0]+1;
  SApath.close();
  pathsa<<min_path[0]+1;
  pathsa.close();
  printf("Minimum cost obtained For Simulated Annealing is=%d\n",getCost(min_path));
  SAdistance << " Minimum Cost: " << getCost(min_path);
  SAdistance.close();
}

int main()
{
srand(time(NULL));
get();
int r1,r2;
clock_t start_t,end_t, total_t;
//clock_t start_t1,end_t1, total_t3;
//clock_t start_t2,end_t2, total_t4;
double random_number,prob,gain;
double temperature=100000000000000;
double absoluteTemperature=1;
init();
start_t=clock();
SApath.open("SApath.txt");
SAtime.open("SAtime.txt");
pathsa.open("pathsa.txt");
//pathsa<<"SA path:"<<"\n";
SAdistance.open("SAdistance.txt");
cout<<"Start For Simulated Annealing="<<start_t<<endl;
while(temperature>absoluteTemperature)
  {
   int i=100;
   while(--i)
   {
    for(int i=1;i<n;i++)
	{
		    
    new_path[i]=curr_path[i];  
    }
    r1=generateRandomNumber();
    r2=generateRandomNumber();
   
    two_opt(r1, r2, new_path);

    gain=getCost(new_path) - getCost(curr_path);
   
    random_number=(double) (rand()/ (double) RAND_MAX);

    prob=1/(1+ pow(M_E, (gain/temperature)));
    if(prob > 	random_number)
     for(int i=1;i<n;i++)    
       curr_path[i]=new_path[i];
    
   
    if(getCost(new_path) < getCost(min_path) )
    {
     for(int i=1;i<n;i++)
	 {
		   
      min_path[i]=new_path[i];
  }
    // end_t = clock(); 
    // cout<<"end="<<end_t<<endl;
     
    //retraceMinPath();
    }
    /*else
    {
    	printf("\nThere is no path of minimum distance\n");
	}*/
   }
   temperature*=0.01;
  }
  retraceMinPath(min_path);
  end_t = clock();
  cout<<"End For Simulated Annealing="<<end_t<<endl;
 double total1 = ((double)(end_t - start_t))/CLOCKS_PER_SEC;
   printf("Total time taken by CPU For Simulate Annealing: %.20f\n", total1  );
   SAtime<<"Time="<<total1;
   SAtime.close();

 
return 0;
}
