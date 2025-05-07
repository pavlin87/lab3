#include <cmath>
#include<iostream>
#define X_START         -3
#define X_FINITE        7

using namespace std;

void Input(float& X0,float& X1,float& dx)
{
    cout << "Input X0: " << endl;
    cin >> X0;
    cout << "Input X1: " << endl;
    cin >> X1;
    cout << "Input dx: " << endl;
    cin >> dx;
}

double func(float x)
{
    if(x>=-3 && x<=-1)
        return -x-1;
    if(x>-1 && x <=1)
        return 0;
    if(x>1 && x<=5)
        return sqrt(4-((x-3)*(x-3)));
    if(x>5 && x<=7)
        return -x/2+2.5;
    return 0;
}

void Output(float X0,float X1,float dx)
{
    cout << "x" << "\t\t" << "y" << endl;
    cout << endl;
    for(float x = X0;x<=X1;x+=dx)
    {
        cout << x << "\t\t" << func(x) << endl;
    }
}

int main()
{
    float X0,X1,dx;
    Input(X0,X1,dx);
    if(dx<=0 || X0<X_START || X1>X_FINITE)
    {
        cout << "Error" << endl;
        exit(1);
    }
    Output(X0,X1,dx);
}
