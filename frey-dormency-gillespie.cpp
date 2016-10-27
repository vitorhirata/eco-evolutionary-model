#include <iostream>
#include <random>
#include <fstream>
#include <cmath>
#define MAX_IT 100
#define RODADAS 100000

using namespace std;
static std::mt19937_64 rand64(time(NULL));
static std::uniform_real_distribution<double> uni(0.0,1.0);
double proximo_tempo (double random1, double alfa);
double media (double vetor[]);
double variancia (double vetor[],double media);
double fC (double a[][2], double C, double D, double s);
double fD (double a[][2], double C, double D, double s);

int main(){
  double C[MAX_IT], D[MAX_IT], t[MAX_IT], random1, random2, tau, alfa[5], beta, a[2][2],N,s,p;
  int i;
  fstream arquivo;
  arquivo.open("txt/frey-dormency-gillespie.txt",ios::out);
  C[0]=2; D[0]=2;t[0]=0;
//  a[0][0]=3; a[0][1]=1; a[1][0]=1; a[1][1]=3; // Equilibrio externo
//  a[0][0]=1; a[0][1]=3; a[1][0]=3; a[1][1]=1; // Equilibrio interno
  a[0][0]=2; a[0][1]=-1; a[1][0]=3; a[1][1]=0;  // Dilema do prisioneiro do Frey
  beta=1/100;
  s=0.1;
  p=10;

  arquivo << t[0] << "   " << C[0] << "  " << D[0] << endl;

  for (i=1; i<MAX_IT; i++){
    random1 = uni(rand64);
    random2 = uni(rand64);
    N = C[i-1]+D[i-1];
    alfa[1] = 0; //C morre
    alfa[2] = (1+p*C[i-1]/N-beta*N)*fC(a,C[i-1],D[i-1],s)*C[i-1]; //C nasce
    alfa[3] = 0; //D morre
    alfa[4] = (1+p*C[i-1]/N-beta*N)*fD(a,C[i-1],D[i-1],s)*D[i-1]; //D nasce
    alfa[0] = alfa[1] + alfa[2] + alfa[3] + alfa[4];

    tau = proximo_tempo(random1,alfa[0]);
    t[i] = t[i-1]+tau;
    if(random2 < alfa[1]/alfa[0]){
      C[i] = C[i-1]-1;
      D[i] = D[i-1];
    }
    else if (random2 < (alfa[1]+alfa[2])/alfa[0]) {
      C[i] = C[i-1]+1;
      D[i] = D[i-1];
    }
    else if (random2 < (alfa[1]+alfa[2]+alfa[3])/alfa[0]) {
      C[i] = C[i-1];
      D[i] = D[i-1]-1;
    }
    else{
      C[i] = C[i-1];
      D[i] = D[i-1]+1;
    }

    arquivo << t[i] << "   " << C[i] << "  " << D[i] << endl;
  }

  arquivo.close();
  return 0;
}


double proximo_tempo (double random1, double alfa){
  return log(1/random1)/(alfa);
}

double media (double vetor[]){
  int i;
  double soma=0;
  for(i=0;i<RODADAS;i++)
    soma+=vetor[i];
  return soma/RODADAS;
}

double variancia (double vetor[],double media){
  int i;
  double variancia=0;
  for(i=0;i<RODADAS;i++)
    variancia+= (media-vetor[i])*(media-vetor[i]);
  return variancia/(RODADAS-1);
}

double fC (double a[][2], double C, double D, double s){
  double f1, f2, N =C+D;
  f1 = 1+s*(a[0][0]*C/N+a[0][1]*D/N);
  f2 = 1+s*(a[1][0]*C/N+a[1][1]*D/N);
  return f1/(f1*C/N+f2*D/N);
}

double fD (double a[][2], double C, double D, double s){
    double f1, f2, N =C+D;
    f1 = 1+s*(a[0][0]*C/N+a[0][1]*D/N);
    f2 = 1+s*(a[1][0]*C/N+a[1][1]*D/N);
    return f2/(f1*C/N+f2*D/N);
}
