#include<stdio.h>
#include<math.h>

#define K 1.95E5
#define gammaL 0.318
#define gammaH 0.472
#define EPS 0.0001

double f1(double N);
double f2(double N);

int main(){
  int i,dia;
  double k1C, k2C, k3C, k4C, h, Ncrit;
  double N, N_ant, N_aux, t;
  double Df, XX;
  FILE *dados1, *dados2, *dados3, *dados4, *dados5,*dados6, *dados7, *dados8, *dados9, *dados10;

  dados1 = fopen("txt/pontofixo-sanchez1.txt", "w");
  h = 0.0005;
  Ncrit = 276;
  XX = 260;
  for(Df=678;Df<3068.4;Df+=20){  //Df = 678 é o mínimo e 3068.4 é o máximo
    dia=0;
    t=0;
    N=K;
    N = N / Df;
    N_ant = 0;  // valor de N no começo do dia
    N_aux = N; // variavel auxiliar para guardar o valor de N no começo do laço, após diluição

    //Calcula ponto fixo estavel
    while(fabs(N-N_ant) > EPS/1000){
      t = t + h;

      if(t > 3){
        if (N < Ncrit){
          k1C = h * f1(N);
          k2C = h * f1(N + k1C / 2);
          k3C = h * f1(N + k2C / 2);
          k4C = h * f1(N + k3C);
          N = N + (k1C + 2 * k2C + 2 * k3C + k4C) / 6;
        }
        else{
          k1C = h * f2(N);
          k2C = h * f2(N + k1C / 2);
          k3C = h * f2(N + k2C / 2);
          k4C = h * f2(N + k3C);
          N = N + (k1C + 2 * k2C + 2 * k3C + k4C) / 6;
        }
        if(fabs(t-23.5) < EPS){ // Se tiver no tempo 23.5 horas
          t = 0;
          dia++;
          N = N / Df;
          N_ant = N_aux;
          N_aux = N;

       }
      }// if t > 3
     } // while dia

     fprintf(dados1, "%f  %f   ", Df,N*Df);

     //Calcula o ponto fixo instavel
     N = XX;
     N_ant = N+.001;
     while (N < N_ant){
       N = N_ant + 10;
       N_ant = N;
       N = N / Df;
       for(t=0;fabs(t-23.5) > EPS; t+= h){
         if(t > 3){
           if (N < Ncrit){
             k1C = h * f1(N);
             k2C = h * f1(N + k1C / 2);
             k3C = h * f1(N + k2C / 2);
             k4C = h * f1(N + k3C);
             N = N + (k1C + 2 * k2C + 2 * k3C + k4C) / 6;
           }
           else{
             k1C = h * f2(N);
             k2C = h * f2(N + k1C / 2);
             k3C = h * f2(N + k2C / 2);
             k4C = h * f2(N + k3C);
             N = N + (k1C + 2 * k2C + 2 * k3C + k4C) / 6;
           }
         }
       } //fim de um dia
       //printf("%f %f %f %f\n",N_ant, N, N-N_ant, Df);
     }
  //  printf("\n");
     XX=N_ant;
     fprintf(dados1, "%f \n",N_ant);

   } // for Df

  fclose(dados1);
  return 0;
}


double f1(double N){
  return gammaL*N;
}

double f2(double N){
  return gammaH*N*(1-N/K);
}
