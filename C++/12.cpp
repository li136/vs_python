#include<cmath>
#include<iostream>
#include<cstdio>
#include<iomanip>//setprecision
using namespace std;
int main(){
	float a,b,c;
	float beta;
	int n;
	cin>>n;
	while(n--){
	cin>>a>>b>>c;
	beta=(b*b*1.0-4*a*c);
	if(beta>0){
		cout<<"x1="<<setprecision(5)<<";"<<(-b+sqrt(beta))/(2*a);
		cout<<"x2="<<setprecision(5)<<(-b-sqrt(beta))/(2*a)<<endl;
	}else if(beta==0){
		cout<<"x1=x2="<<setprecision(5)<<(-b)*1.0/(2*a)<<endl;
	}else{
		float rpart=(-b)*1.0/(2*a);//实部
		float ipart=sqrt(-beta)*1.0/(2*a);//虚部
		cout<<"x1="<<setprecision(5)<<rpart<<"+"<<ipart<<"i;";
		cout<<"x2="<<setprecision(5)<<rpart<<"-"<<ipart<<"i"<<endl;
	}
	}
	return 0;
}