//Implement a program that prints the first 10 numbers of Fibonacci sequence.

#include<stdio.h>
int main()
{
	int t1=0,t2=1;
	int nxt_term,n,i;
	
	// the asked is 10.
	n = 10;
	printf("The integer is 10\n");
		
	nxt_term = t1+t2;
	printf("The Fibonacci sequence is: %d, %d, %d",t1,t2,nxt_term);
	
	
	for(i=3;i<=n;++i)
	{
		printf("%d, ",nxt_term);
		t1 = t2;
    	t2 = nxt_term;
    	nxt_term = t1 + t2;
		
	 } 
	
	return 0;
}
