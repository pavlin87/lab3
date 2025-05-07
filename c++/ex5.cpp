#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
double T;
double Ts;
double r;
int time_limit;
pair<double,double> aproxCof;

double korrel(const vector<double>& temperatures,double mean_y,int t)
{
    double sum_xy=0,sum_x=0,sum_y=0;
    double mean_x=(time_limit-1)/2.0;
    for(int x=0;x<=t;x++)
    {
        sum_xy+=(x-mean_x)*(temperatures[x]-mean_y);
        sum_x+=(x-mean_x)*(x-mean_x);
        sum_y+=(temperatures[x]-mean_y)*(temperatures[x]-mean_y);
    }
    return sum_xy/ sqrt(sum_x*sum_y);
}

pair<double,double> aprox(const vector<double>& x,const vector<double>& y)
{
    int n = x.size();
    double sum_xy=0,sum_x=0,sum_y=0,sum_x2=0;
    for(int i=0;i<n;i++)
    {
        sum_xy+=x[i]*y[i];
        sum_x+=x[i];
        sum_y+=y[i];
        sum_x2+=x[i]*x[i];
    }
    double a = (n*sum_xy-sum_x*sum_y)/(n*sum_x2-sum_x*sum_x);
    double b = (sum_y-a*sum_x)/n;
    pair<double,double> approx_coef(0.0,0.0);
    approx_coef.first = a;
    approx_coef.second = b;
    return approx_coef;
}

vector<pair<double,double>> coffee(double T,double Ts,double r,double time_limit)
{
    vector<double> temperatures;
    vector<double> time;
    vector<pair<double,double>> temperatures_corr;
    for(int t=0;t<=time_limit;t++)
    {
        temperatures.push_back(Ts+(T-Ts)*exp(-r*t));
        time.push_back(t);
    }

    double mean_y=0;
    for(int i=0;i<=temperatures.size();i++) 
    {
        mean_y+=temperatures[i];
    }   
    mean_y=mean_y/temperatures.size();
    for(int t=0;t<=time_limit;t++)
    {
        temperatures_corr.push_back({temperatures[t],korrel(temperatures,mean_y,t)});
    }    
    aproxCof=aprox(time,temperatures);
    return temperatures_corr;
}

int main()
{
    cout<<"T: "<<endl;
    cin>>T;
    cout<<"Ts: "<<endl;
    cin>>Ts;
    cout<<"r: "<<endl;
    cin>>r;
    cout<<"time_limit: "<<endl;
    cin>>time_limit;
    vector<pair<double,double>> t_c = coffee(T,Ts,r,time_limit);
    cout<<"коэффициенты аппроксимирующей прямой: a =  "<< aproxCof.first<<"\t"<<"b = "<< aproxCof.second<<endl;;
    cout<<"Время"<<"\t"<<"Температура"<<"\t"<<"Коэф Корреляции"<<endl;;
    int t=0;
    for(const auto& res:t_c)
    {
        cout<<t<<"\t"<<res.first<<"\t\t"<<res.second<<endl;
        t++;
    }
}

