#include <iostream>
#include <random>
#include <fstream>
#include <cmath>
#define MAX 1000

using namespace std;
static std::mt19937_64 rand64(time(NULL));
static std::uniform_real_distribution<double> uni(0.0,1.0);

double proximo_tempo (double random, double x, double rate_conversion){
  return log(1/random)/(x*rate_conversion);
}

int main(){
  double x[MAX], t[MAX], random, tau, rate_conversion;
  int i;
  fstream arquivo;
  arquivo.open("txt/decaimento.txt",ios::out);
  x[0]=50;t[0]=0;
  rate_conversion = 0.01;
  arquivo << t[0] << "   " << x[0] << endl;

  for (i=1; i<MAX; i++){
    random = uni(rand64);
    tau = proximo_tempo(random,x[i-1], rate_conversion);
    t[i] = t[i-1]+tau;
    x[i] = x[i-1]-1;

    if(x[i] < 0)
      break;

    arquivo << t[i] << "   " << x[i] << endl;
  }

  arquivo.close();
  return 0;
}
