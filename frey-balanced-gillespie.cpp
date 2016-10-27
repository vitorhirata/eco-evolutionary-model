#include <iostream>
#include <random>
#include <fstream>
#include <cmath>
#define MAX_IT 20000
#define MAX_ROD 1000
#define b 3
#define c 1

using namespace std;
static std::mt19937_64 rand64(time(NULL));
static std::uniform_real_distribution<double> uni(0.0,1.0);
double proximo_tempo (double random1, double alfa);
double media (double vetor[]);
double variancia (double vetor[],double media);
double fC (double a[][2], double C, double D, double s);
double fD (double a[][2], double C, double D, double s);

int main(){
  double C[MAX_ROD], D[MAX_ROD], t[MAX_ROD], mediaC, mediaD, mediat;
  double random1, random2, tau, alfa[5], beta, N , s , p, a[2][2];
  int i, j;
  fstream arquivo1, arquivo2;
  arquivo1.open("txt/frey-balanced-gillespie1.txt",ios::out);
  arquivo2.open("txt/frey-balanced-gillespie2.txt",ios::out);

//  a[0][0]=3; a[0][1]=1; a[1][0]=1; a[1][1]=3; // Equilibrio externo
//  a[0][0]=1; a[0][1]=3; a[1][0]=3; a[1][1]=1; // Equilibrio interno
  a[0][0]=2; a[0][1]=-1; a[1][0]=3; a[1][1]=0;  // Dilema do prisioneiro do Frey

  beta=1/110.0;
  s=0.1;
  p=10;

  for(j=0;j<MAX_ROD;j++){
    C[j]=2; D[j]=2;t[j]=0; // Condicao inicial do sistema
  }

  for (i=0; i<MAX_IT; i++){
    for (j=0; j < MAX_ROD; j++){
      random1 = uni(rand64);
      random2 = uni(rand64);
      N = C[j] + D[j];
      alfa[1] = beta*N*C[j]; //C morre
      alfa[2] = (1+p*C[j]/N)*fC(a,C[j],D[j],s)*C[j]; //C nasce
      alfa[3] = beta*N*D[j]; //D morre
      alfa[4] = (1+p*C[j]/N)*fD(a,C[j],D[j],s)*D[j]; //D nasce
      alfa[0] = alfa[1] + alfa[2] + alfa[3] + alfa[4];
      tau = proximo_tempo(random1,alfa[0]);
      t[j] = t[j]+tau;
      if(random2 < alfa[1]/alfa[0])
        C[j] = C[j]-1;
      else if (random2 < (alfa[1]+alfa[2])/alfa[0])
        C[j] = C[j]+1;
      else if (random2 < (alfa[1]+alfa[2]+alfa[3])/alfa[0])
        D[j] = D[j]-1;
      else
        D[j] = D[j]+1;

    }
    mediat = media(t);
    mediaC = media(C);
    mediaD = media(D);
    arquivo1 << mediat << "   " << mediaC + mediaD << endl;
    arquivo2 << mediat << "   " << mediaC / (mediaC + mediaD) << endl;
  }

  arquivo1.close();
  arquivo2.close();
  return 0;
}


double proximo_tempo (double random1, double alfa){
  return log(1/random1)/(alfa);
}

double media (double vetor[]){
  int j;
  double soma=0;

  for(j=0;j<MAX_ROD;j++)
    soma+=vetor[j];
  return soma/MAX_ROD;
}

double variancia (double vetor[],double media){
  int j;
  double variancia=0;
  for(j=0;j<MAX_ROD;j++)
    variancia+= (media-vetor[j])*(media-vetor[j]);
  return sqrt(variancia/(MAX_ROD-1));
}


double fC (double a[][2], double C, double D, double s){
  double f1, ft, N =C+D;
  f1 = 1 + s*(b * C/N - c);
  ft = 1 + s*(b - c) * C/N;

  return f1/ft;
}

double fD (double a[][2], double C, double D, double s){
    double f2, ft, N =C+D;
    f2 = 1+s*b*C/N;
    ft = 1 + s*(b - c) * C/N;
    return f2/ft;
}
