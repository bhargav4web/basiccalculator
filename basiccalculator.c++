#include<iostream>
using namespace std;

int main()
{
	char op;
	int num1,num2;
	
	cout<<"enter the operator + or - or * or / ";
	cin>>op;

	cout<<"enter two operands: ";
	cin>>num1>>num2;
	
	switch(op)
	{
		case '+':
		cout<<num1+num2;
		break;
		

		case '-':
		cout<<num1-num2;
		break;
		
		case '*':
		cout<<num1*num2;
		break;
		
		case '/':
		cout<<num1/num2;
		break;
		#if the input is other than the operators#
		default:
		cout<<"invalid input";
	}
	
	return 0;

}
