/* Adds the death rate */

#include <iostream>
#include <random>
#include <fstream>
#include <cmath>
#define MAX_IT 100000
#define MAX_ROD 3
#define EPS 0.005t

using namespace std;
static std::mt19937_64 rand64(time(NULL));
static std::uniform_real_distribution<double> uni(0.0,1.0);
double proximo_tempo (double random1, double alfa);
double media (double vetor[]);
double variancia (double vetor[],double media);

int main(){
  double C[MAX_ROD], D[MAX_ROD], t[MAX_ROD], random1, random2, tau, alfa[5], beta, a[2][2],N, mediaC, mediaD;
  int i,j,k,l[MAX_ROD];
  fstream arquivo, arquivo2;
  arquivo.open("txt/dai-gillespie-A1_add-death.txt",ios::out);
  arquivo2.open("txt/dai-gillespie-A2_add-death.txt",ios::out);
  beta=.00001;
  a[0][0]=1; a[0][1]=1; a[1][0]=1; a[1][1]=4; // Equilibrio externo
//  a[0][0]=1; a[0][1]=3; a[1][0]=3; a[1][1]=1; // Equilibrio interno
//  a[0][0]=2; a[0][1]=-1; a[1][0]=3; a[1][1]=0; // Dilema do prisioneiro do Frey

//  arquivo << t[0] << " " << C[0] << " " << 0 << " " << D[0] << " " << 0 << endl;

  for(k=0;k < 1; k++){

    for(j=0;j<MAX_ROD;j++){
      C[j]=pow(2,k)*700; D[j]=0;t[j]=0;l[j]=1; // Condicao inicial do sistema
    }

    for (i=1; i<MAX_IT; i++){
      for(j=0;j<MAX_ROD;j++){
        random1 = uni(rand64) ;
        random2 = uni(rand64);
        N = C[j]+D[j];
        alfa[1] = beta*N*C[j]; //C morre
        alfa[2] = (1+a[0][0]*C[j]/N+a[0][1]*D[j]/N)*C[j]; //C nasce
        alfa[3] = beta*N*D[j]; //D morre
        alfa[4] = (1+a[1][0]*C[j]/N+a[1][1]*D[j]/N)*D[j]; //D nasce
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

        if(fabs(t[j]-l[j]*0.5) < EPS){
          l[j]++;
          arquivo << t[j] << "   " << C[j] << endl;
          C[j] = C[j] / 10;
          //arquivo2 << C[j] << endl;
        }
      }
    }
  }
  arquivo.close();
  arquivo2.close();
  return 0;
}


double proximo_tempo (double random1, double alfa){
  return log(1/random1)/(alfa);
}

double media (double vetor[]){
  int i;
  double soma=0;

  for(i=0;i<MAX_ROD;i++)
    soma+=vetor[i];
  return soma/MAX_ROD;
}

double variancia (double vetor[],double media){
  int i;
  double variancia=0;
  for(i=0;i<MAX_ROD;i++)
    variancia+= (media-vetor[i])*(media-vetor[i]);
  //return sqrt(variancia/(MAX_ROD-1));
  return 0;
}
