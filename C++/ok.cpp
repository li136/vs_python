#include<iostream>
#include<cstdio>
using namespace std;
int status[12];
char left1[3][7],right[3][7],result[3][7];

bool Balanced(){
	int i,k,leftW,rightW;
	for(i=0;i<3;i++){
		leftW=rightW=0;
		for(k=0;k<6&&left1[i][k]!=0;k++){
			leftW +=status[left1[i][k]-'A'];
			rightW +=status[right[i][k]-'A'];
		}
		if(leftW>rightW&&result[i][0]!='u')
		    return false;
		if(leftW==rightW&&result[i][0]!='e')
		    return false;
		if(leftW<rightW&&result[i][0]!='d')
		    return false;
	}
	return true;
}
int main(){
    int i,num;
	cin>>num;
	while(num>0){
        num--;
		for(i=0;i<3;i++)
		   cin>>left1[i]>>right[i]>>result[i];
		for(i=0;i<12;i++)
           status[i]=0;
        for(i=0;i<12;i++){
        	status[i]=1;     //第i枚硬币是较重假币
        	if(Balanced())
        	   break;
        	status[i]= -1;   //第i枚硬币是较轻假币
        	if(Balanced())
               break;
            status[i]=0;     //       
		}
		cout<<i+'A'<<"is the counterfeit cion and it is"<<(status[i]>0)?"heavy":"light";
 	}	
 	return 0;
}