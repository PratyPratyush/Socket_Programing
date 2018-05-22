#include<iostream>
#include<vector>
using namespace std;
int main()
{
long long i,n,j,s,t,l=0,flag=0;

cin>>t;
for(int k=0;k<t;k++)
{
l=0;
vector <long long> v;
cout<<"Enter size of array";
cin>>n;
long long a[n];
for(i=0;i<n;i++)
{
cin>>a[i];
}
cin>>s;
for(i=0,j=n-1;i<j;i++,j--)
{
l=l+a[i];
v.push_back(i);
if(l==s)
{
flag=1;
break;
}
else
{
l=l+a[j];
v.push_back(j);
if(l==s)
{
flag=1;
break;

}
}
}
if(flag==1)
{
cout<<"Success"<<endl;
}
else
{
cout<<"Not Success"<<endl;
}
for(i=0;i<v.size();i++)
{
cout<<v[i]<<" ";
}
cout<<endl;
}


}
