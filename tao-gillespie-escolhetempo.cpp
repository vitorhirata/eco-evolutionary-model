#include <iostream>
#include <random>
#include <fstream>
#include <cmath>
#define MAX_IT 5000
#define MAX_ROD 1
#define EPSILON .001

using namespace std;
static std::mt19937_64 rand64(time(NULL));
static std::uniform_real_distribution<double> uni(0.0,1.0);
double proximo_tempo (double random1, double alfa);
double calcula_media (double vetor[]);
double calcula_variancia (double vetor[], double media);
bool mesmo_tempo (double t1, double t2);
void menor(double tempo[][MAX_ROD], int *i_saida, int *j_saida);

int main(){
  /* C e D são do tipo: tempo X rodada*/
  double C[MAX_IT][MAX_ROD], D[MAX_IT][MAX_ROD], C_igual[MAX_ROD],D_igual[MAX_ROD], t[MAX_IT][MAX_ROD];
  double random1, random2, tau, alfa[5], beta, a[2][2],N, mediaC, mediaD, t_igual;
  int i,j, k;
  bool condicao=true;
  fstream arquivo;
  arquivo.open("txt/tao-gillespie-escolhetempo.txt",ios::out);
  beta=.01;
  a[0][0]=3; a[0][1]=1; a[1][0]=1; a[1][1]=3; // Equilibrio externo
//  a[0][0]=1; a[0][1]=3; a[1][0]=3; a[1][1]=1; // Equilibrio interno
//  a[0][0]=2; a[0][1]=-1; a[1][0]=3; a[1][1]=0; // Dilema do prisioneiro do Frey
  for(j=0; j<MAX_ROD;j++){
    C[0][j]=350; D[0][j]=50; t[0][j]=0;
  }

  arquivo << t[0][0] << "   " << C[0][0]/400 << "  " << D[0][0]/400 << endl;

  for(j=0;j<MAX_ROD;j++){
    for (i=1; i<MAX_IT; i++){
      random1 = uni(rand64);
      random2 = uni(rand64);
      N = C[i-1][j]+D[i-1][j];
      alfa[1] = beta*N*C[i-1][j]; //C morre
      alfa[2] = (1+a[0][0]*C[i-1][j]/N+a[0][1]*D[i-1][j]/N)*C[i-1][j]; //C nasce
      alfa[3] = beta*N*D[i-1][j]; //D morre
      alfa[4] = (1+a[1][0]*C[i-1][j]/N+a[1][1]*D[i-1][j]/N)*D[i-1][j]; //D nasce
      alfa[0] = alfa[1] + alfa[2] + alfa[3] + alfa[4];

      tau = proximo_tempo(random1,alfa[0]);
      t[i][j] = t[i-1][j]+tau;
      if(random2 < alfa[1]/alfa[0]){
        C[i][j] = C[i-1][j]-1;
        D[i][j] = D[i-1][j];
      }
      else if (random2 < (alfa[1]+alfa[2])/alfa[0]) {
        C[i][j] = C[i-1][j]+1;
        D[i][j] = D[i-1][j];
      }
      else if (random2 < (alfa[1]+alfa[2]+alfa[3])/alfa[0]) {
        C[i][j] = C[i-1][j];
        D[i][j] = D[i-1][j]-1;
      }
      else{
        C[i][j] = C[i-1][j];
        D[i][j] = D[i-1][j]+1;
      }
    }
  }

  while(condicao){

    for(j=0;j<MAX_ROD;j++)
      C_igual[j]=D_igual[j]=0;

    menor(t, &i, &j);
    C_igual[0] = C[i][j];
    D_igual[0] = D[i][j];
    t_igual=t[i][j];
    C[i][j]=D[i][j]=t[i][j]=10*MAX_IT;
    k=1;

    for(j=0;j<MAX_ROD;j++)
      for(i=0;i<MAX_IT;i++)
        if(mesmo_tempo(t[i][j],t_igual)){
          C_igual[k]=C[i][j];
          D_igual[k]=D[i][j];
          k++;
          C[i][j]=D[i][j]=t[i][j]=10*MAX_IT;
        }
    C_igual[k]=D_igual[k]=10*MAX_IT;
    mediaC = calcula_media(C_igual);
    mediaD = calcula_media(D_igual);
    arquivo << t[i][j] << " " << mediaC/N << " " << calcula_variancia(C_igual,mediaC) << " ";
    arquivo <<  mediaD/N << " " << calcula_variancia(D_igual,mediaD) << endl;

    condicao = false;
    for(j=0;j<MAX_ROD;j++)
      if(C[MAX_IT][j] != 10*MAX_IT){
        condicao=true;
        break;
      }
  }



  arquivo.close();
  return 0;
}


double proximo_tempo (double random1, double alfa){
  return log(1/random1)/(alfa);
}

double calcula_media (double vetor[]){
  int i;
  double soma=0;
  for(i=0;vetor[i] != 10*MAX_IT;i++)
    soma+=vetor[i];
  return soma/i;
}

double calcula_variancia (double vetor[],double media){
  int i;
  double variancia=0;
  for(i=0;vetor[i] != MAX_IT;i++)
    variancia+= (media-vetor[i])*(media-vetor[i]);
  return variancia/(i-1);
}

bool mesmo_tempo (double t1, double t2){
  if (abs(t1 - t2) < EPSILON)
    return true;
  else
    return false;
}

void menor(double tempo[][MAX_ROD], int *i_saida, int *j_saida){
  int i,j, i_menor, j_menor;
  double menor = 10*MAX_IT; // valor grande

  for(j=0;j<MAX_ROD;j++){
    for(i=0;i<MAX_IT && (i==0 || tempo[i-1][j] == 10*MAX_IT);i++)
      if(tempo[i][j] < menor){
        menor = tempo[i][j];
        i_menor=i;
        j_menor=j;
      }
  } //fecha ultimo loop
  *i_saida = i_menor;
  *j_saida = j_menor;
}
