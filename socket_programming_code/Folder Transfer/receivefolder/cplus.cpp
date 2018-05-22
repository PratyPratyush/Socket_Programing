#include<iostream>
using namespace std;
int main()
{
int i,j;
string s[2][2];
for(i=0;i<2;i++)
{
for(j=0;j<2;j++)
{
cout<<"Enter value";
cin>>s[i][j];
}
}
for(i=0;i<2;i++)
{
for(j=0;j<2;j++)
{
cout<<s[i][j]<<"\t";
}
}
return 0;
}
