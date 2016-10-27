#include <iostream>
#include <random>
#include <fstream>
#include <cmath>
#define MAX_IT 1000000

using namespace std;
static std::mt19937_64 rand64(time(NULL));
static std::uniform_real_distribution<double> uni(0.0,1.0);
double proximo_tempo (double random1, double alfa);

int main(){
  double C, D, t, random1, random2, tau, alfa[5], beta, a[2][2],N;
  int i;
  fstream arquivo;
  arquivo.open("txt/tao-gillespie-simples.txt",ios::out);
  C=2; D=0;t=0;
  a[0][0]=1; a[0][1]=1; a[1][0]=1; a[1][1]=3; // Equilibrio externo
//  a[0][0]=1; a[0][1]=3; a[1][0]=3; a[1][1]=1; // Equilibrio interno
//  a[0][0]=2; a[0][1]=-1; a[1][0]=3; a[1][1]=0; // Dilema do prisioneiro do Frey
  beta=.0001;

  arquivo << t << "   " << C << endl;

  for (i=1; i < MAX_IT; i++){
    random1 = uni(rand64);
    random2 = uni(rand64);
    N = C+D;
    alfa[1] = beta*N*C; //C morre
    alfa[2] = (1+a[0][0]*C/N+a[0][1]*D/N)*C; //C nasce
    alfa[3] = beta*N*D; //D morre
    alfa[4] = (1+a[1][0]*C/N+a[1][1]*D/N)*D; //D nasce
    alfa[0] = alfa[1] + alfa[2] + alfa[3] + alfa[4];

    tau = proximo_tempo(random1,alfa[0]);
    t = t+tau;
    if(random2 < alfa[1]/alfa[0]){
      C = C-1;
      D = D;
    }
    else if (random2 < (alfa[1]+alfa[2])/alfa[0]) {
      C = C+1;
      D = D;
    }
    else if (random2 < (alfa[1]+alfa[2]+alfa[3])/alfa[0]) {
      C = C;
      D = D-1;
    }
    else{
      C = C;
      D = D+1;
    }

    arquivo << t << " " << C << endl;
  }

  arquivo.close();
  return 0;
}


double proximo_tempo (double random1, double alfa){
  return log(1/random1)/(alfa);
}
