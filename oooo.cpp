#include<stdio.h>
#define n 5
int main()
{
	int  X[n][n]={{0,0,1,0,0},
	{0,0,0,0,1},
	{0,0,0,1,0},
	{0,1,0,0,0},
	{1,0,0,0,0},};
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(X[i][j]==1)
			{
				printf("%d",j+1);
				i=j;
				j=0;		
			}
		}
	}
	return 0;
}
