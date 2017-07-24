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
#include <sstream>
#include <string>
#include <vector>
#include<stdlib.h>
//#define size 10 
#define min(a,b) a>b?b:a
#define sizePOW 1024
using namespace std;
ofstream GApath;
ofstream pathga; 
ofstream GAdistance;
ofstream GAtime;
ifstream nvalue;
int npow,g[1000][1024],p[1000][1024];
 int originalGraph[100][100];
 int points[10000][2],n;
 int visited[10000],cost=0;
 int real_size_population = 0;
int 	generations =1000 ;
int	mutation_rate = 5;
vector<pair<vector<int>, int> >population;
bool show_population = true;
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


//Genetic algorithm
void insertBinarySearch(vector<int>& child, int total_cost)
{
	int imin = 0;
	int imax = real_size_population - 1;
	
	while(imax >= imin)
	{
		int imid = imin + (imax - imin) / 2;
		
		if(total_cost == population[imid].second)
		{
			population.insert(population.begin() + imid, make_pair(child, total_cost));
			return;
		}
		else if(total_cost > population[imid].second)
			imin = imid + 1;
		else
			imax = imid - 1;
	}
	population.insert(population.begin() + imin, make_pair(child, total_cost));
}
bool existsChromosome(const vector<int> & v)
{
	
	for(vector<pair<vector<int>, int> >::iterator it=population.begin(); it!=population.end(); ++it)
	{
		const vector<int>& vec = (*it).first; // gets the vector
		if(equal(v.begin(), v.end(), vec.begin())) // compares vectors
			return true;
	}
	return false;
}

int isValidSolution(vector<int>& solution)
{
	int total_cost=0;
	set<int>set_solution;
	for(int i=0;i<n;i++)
	{
		set_solution.insert(solution[i]);
	}
	if(set_solution.size()!=n)
	{
		return -1;
	}
	//check if connection are valid or not
	for(int i=0;i<n;i++)
	{
		if(i+1<n)
		{
		int cost=originalGraph[solution[i]][solution[i+1]];	
		if(cost == -1)
				return -1;
			else
				total_cost += cost;
		}
		else
		{
			int cost=originalGraph[solution[i]][solution[0]];
			if(cost == -1)
				return -1;
			else
				total_cost += cost;
		}
	}
	return total_cost;
}
bool sortbysec(const pair<vector<int>,int> &a,
              const pair<vector<int>,int> &b)
{
    return (a.second < b.second);
}
void initialpopulation()
{
	vector<int> parent;
	parent.push_back(0);
	for(int i=1;i<n;i++)
	{
		parent.push_back(i);
	}
	int total_cost=isValidSolution(parent);
//	vector<pair<vector<int>, int> >population;
	//printf("Initial Cost=%d\n",total_cost);
	if(total_cost != -1) // checks if the parent is valid
	{
		population.push_back(make_pair(parent, total_cost)); 
		real_size_population++; 
	}
	for(int i=0;i<generations;i++)
	{
		random_shuffle(parent.begin() + 1, parent.begin() + (rand() % (n - 1) + 1));
		int total_cost = isValidSolution(parent);
	//	printf("New Cost=%d\n",total_cost);
		if(total_cost != -1)
		{
		    population.push_back(make_pair(parent, total_cost)); 
			real_size_population++; 
		}
		if(real_size_population == n) // checks size population
			break;
			
	}
	if(real_size_population == 0)
		cout << "\nEmpty initial population ;( Try again runs the algorithm...";
	
	sort(population.begin(), population.end(),  sortbysec);
//	cout<<"real_size_population="<<real_size_population<<endl; 
}
void crossOver(vector<int>& parent1, vector<int>& parent2)
{
	vector<int> child1, child2;
	map<int, int> genes1, genes2;
	for(int i = 0; i<n; i++)
	{
		genes1[parent1[i]] = 0;
		genes2[parent2[i]] = 0;
	}
	int point1 = rand() % (n - 1) + 1;
	int point2 = rand() % (n - point1) + point1;
	if(point1 == point2)
	{
		if(point1 - 1 > 1)
			point1--;
		else if(point2 + 1 <n)
			point2++;
		else
		{
			
			int point = rand() % 10 + 1; 
			if(point <= 5)
				point1--;
			else
				point2++;
		}
	}
	for(int i = 0; i < point1; i++)
	{
		// adds genes
		child1.push_back(parent1[i]);
		child2.push_back(parent2[i]);
		// marks genes
		genes1[parent1[i]] = 1;
		genes2[parent2[i]] = 1;
	}
	for(int i = point2 + 1; i < n; i++)
	{
		genes1[parent1[i]] = 1;
		genes2[parent2[i]] = 1;
	}
	for(int i = point2; i >= point1; i--)
	{
		if(genes1[parent2[i]] == 0) // if the gene is not used
		{
			child1.push_back(parent2[i]);
			genes1[parent2[i]] = 1; // marks the gene	
		}
		else
		{
			// if the gene already is used, chooses gene that is not used
			for(map<int, int>::iterator it = genes1.begin(); it != genes1.end(); ++it)
			{
				if(it->second == 0) // checks if is not used
				{
					child1.push_back(it->first);
					genes1[it->first] = 1; // marks as used
					break; // left the loop
				}
			}
		}
		
		if(genes2[parent1[i]] == 0) // if the gene is not used
		{
			child2.push_back(parent1[i]);
			genes2[parent1[i]] = 1; // marks the gene
		}
		else
		{
			// if the gene already is used, chooses gene that is not used
			for(map<int, int>::iterator it = genes2.begin(); it != genes2.end(); ++it)
			{
				if(it->second == 0) // checks if is not used
				{
					child2.push_back(it->first);
					genes2[it->first] = 1; // marks as used
					break; // left the loop
				}
			}
		}
	
    }
    for(int i = point2 + 1; i < n; i++)
	{
		child1.push_back(parent1[i]);
		child2.push_back(parent2[i]);
	}
	int mutation = rand() % 100 + 1; 
	if(mutation <= mutation_rate) 
	{
		// makes a mutation: change of two genes
		
		int index_gene1, index_gene2;
		index_gene1 = rand() % (n - 1) + 1;
		index_gene2 = rand() % (n - 1) + 1;
		
		// makes for child1
		int aux = child1[index_gene1];
		child1[index_gene1] = child1[index_gene2];
		child1[index_gene2] = aux;
		
		// makes for child2
		aux = child2[index_gene1];
		child2[index_gene1] = child2[index_gene2];
		child2[index_gene2] = aux;
	}
	int total_cost_child1 = isValidSolution(child1);
//	printf("Initial Cost child 1=%d\n",total_cost_child1);
	int total_cost_child2 = isValidSolution(child2);
	if(total_cost_child1 != -1 && !existsChromosome(child1))
	{
		// add child in the population
		insertBinarySearch(child1, total_cost_child1); // uses binary search to insert
		real_size_population++; // increments the real_size_population
	}
	
	// checks again...
	if(total_cost_child2 != -1 && !existsChromosome(child2))
	{
		// add child in the population
		insertBinarySearch(child2, total_cost_child2); 
		real_size_population++; 
	}
}
void geneticrun()
{
	initialpopulation();
	if(real_size_population==0)
	   return;
	for(int i=0;i<generations;i++)
	{
		int old_size_population=real_size_population;
		if(real_size_population>=2)
		{
	     	if(real_size_population==2)
		   {
			crossOver(population[0].first, population[1].first);
	       }
		   else
		   {
		   	int parent1,parent2;
		   	do{
		   		parent1=rand()%real_size_population;
		   		parent2=rand()%real_size_population;
			   }while(parent1==parent2);
			   crossOver(population[parent1].first, population[parent2].first);
		   	
		   }
		   int diff_population = real_size_population - old_size_population;
			
			if(diff_population == 2)
			{
				if(real_size_population > n)
				{
					// removes the two worst parents of the population
					population.pop_back();
					population.pop_back();
					
					// decrements the real_size_population in 2 units
					real_size_population -= 2;
				}
			}
			else if(diff_population == 1)
			{
				if(real_size_population > n)
				{
					population.pop_back(); 
					real_size_population--; 
				}
			}	
		}
		else 
		{
			
			crossOver(population[0].first, population[0].first);
			
			if(real_size_population > n)
			{
				population.pop_back(); 
				real_size_population--; 
			}
		}
	}
	cout <<"Tour sequence For Genetic Algorithm= ";
	const vector<int>& vec = population[0].first;
	for(int i = 0; i < n; i++)
	{
	
		cout << vec[i]+1 << "-->";
		pathga<<vec[i]+1<<"-->";
		int p=vec[i];
		GApath << p+1 <<",";
		
	}
	
	cout << vec[0]+1<<endl;
	GApath << vec[0]+1;
	GApath.close();
	pathga<<vec[0]+1<<endl;
	pathga.close();
//	cout << graph->initial_vertex;
	cout <<"Minimum Cost For Genetic Algorithm: " << population[0].second<<endl;
	GAdistance << " Minimum Cost: " << population[0].second;
	GAdistance.close();
	//cout <<"helloooooooooooo";
    
}

int main()
{
srand(time(NULL));
get();
int r1,r2;
clock_t start_t,end_t, total_t;
clock_t start_t1,end_t1, total_t3;
clock_t start_t2,end_t2, total_t4;

 //minimum distance using Genetic Algorithm
    start_t2=clock();
	cout<<"\n\nstart time for Genetic Algorithm="<<start_t2<<endl;
     GApath.open("GApath.txt");
     pathga.open("pathga.txt");
     //pathga<<"GA path:"<<"\n";
     GAtime.open("GAtime.txt");
     GAdistance.open("GAdistance.txt");
		geneticrun();
		end_t2=clock();
	cout<<"end time for Genetic Algorithm="<<end_t2<<endl;
	double total5 = ((double)(end_t2 - start_t2))/CLOCKS_PER_SEC;
   printf("Total time taken by CPU For Genetic Algorithm: %.20f\n", total5  );
   GAtime<<"Time="<<total5;
   GAtime.close();


return 0;
}
