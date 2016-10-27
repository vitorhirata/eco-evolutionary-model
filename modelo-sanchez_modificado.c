#include<stdio.h>
#include<math.h>

#define K 83341
#define beta 1.1999E-05
#define gammaL 0.31
#define gammaH 0.47
#define a 0.075
#define b 2
#define c 138
#define EPS 0.0001
#define Df 667
#define ni 0.001
#define a11 3
#define a12 -1
#define a21 4
#define a22 0

double f1(double Nc, double Nd);
double g1(double Nc, double Nd);

int main(){
  int i,dia,j;
  double k1C, k2C, k3C, k4C, k1D, k2D, k3D, k4D, h, Ncrit;
  double Nc, Nd, t;
  FILE *dados1, *dados2, *dados3, *dados4, *dados5,*dados6, *dados7, *dados8, *dados9, *dados10;

  dados1 = fopen("txt/modelo-sanchez_modificado1.txt", "w");
  dados2 = fopen("txt/modelo-sanchez_modificado2.txt", "w");
  dados3 = fopen("txt/modelo-sanchez_modificado3.txt", "w");
  dados4 = fopen("txt/modelo-sanchez_modificado4.txt", "w");
  dados5 = fopen("txt/modelo-sanchez_modificado5.txt", "w");
  dados6 = fopen("txt/modelo-sanchez_modificado6.txt", "w");
  dados7 = fopen("txt/modelo-sanchez_modificado7.txt", "w");
  dados8 = fopen("txt/modelo-sanchez_modificado8.txt", "w");
  dados9 = fopen("txt/modelo-sanchez_modificado9.txt", "w");
  dados10 = fopen("txt/modelo-sanchez_modificado10.txt", "w");
  h = 0.0005;
  Ncrit = 276;

  for(i=0;i<10;i++){ // Cuida de cada rodada
    dia=1;
    t=0;
    j=0;
    switch (i) { // printa so a rodada i
      case 0: Nc=135;Nd=8865; fprintf(dados1, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 1: Nc=60;Nd=90; fprintf(dados2, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 2: Nc=240;Nd=60; fprintf(dados3, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 3: Nc=250;Nd=0; fprintf(dados4, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 4: Nc=600;Nd=0; fprintf(dados5, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 5: Nc=480;Nd=120; fprintf(dados6, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 6: Nc=600;Nd=400; fprintf(dados7, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 7: Nc=500;Nd=9500; fprintf(dados8, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 8: Nc=2000;Nd=38000; fprintf(dados9, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 9: Nc=46000;Nd=69000; fprintf(dados10, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
    }
    //Nc = Nc / Df;
    //Nd = Nd / Df; // Diluicao

    while(dia < 2){
      t = t + h;
      if(t > 3){
        k1C = h * f1(Nc, Nd);
        k2C = h * f1(Nc + k1C / 2, Nd);
        k3C = h * f1(Nc + k2C / 2, Nd);
        k4C = h * f1(Nc + k3C, Nd);
        k1D = h * g1(Nc, Nd);
        k2D = h * g1(Nc, Nd + k1D / 2);
        k3D = h * g1(Nc, Nd + k2D / 2);
        k4D = h * g1(Nc, Nd + k3D);
        Nc = Nc + (k1C + 2 * k2C + 2 * k3C + k4C) / 6;
        Nd = Nd + (k1D + 2 * k2D + 2 * k3D + k4D) / 6;

        if(j % 1000 == 0) // printa de 10.000 em 10.000
          //if()
          switch (i) { // printa so a rodada i
            case 0: fprintf(dados1, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
            case 1: fprintf(dados2, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
            case 2: fprintf(dados3, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
            case 3: fprintf(dados4, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
            case 4: fprintf(dados5, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
            case 5: fprintf(dados6, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
            case 6: fprintf(dados7, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
            case 7: fprintf(dados8, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
            case 8: fprintf(dados9, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
            case 9: fprintf(dados10, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
          }
        j++;
        if(fabs(t-23.5) < EPS){ // Se tiver no tempo 23.5 horas
           /*switch (i) { // printa so a rodada i
             case 0: fprintf(dados1, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
             case 1: fprintf(dados2, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
             case 2: fprintf(dados3, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
             case 3: fprintf(dados4, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
             case 4: fprintf(dados5, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
             case 5: fprintf(dados6, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
             case 6: fprintf(dados7, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
             case 7: fprintf(dados8, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
             case 8: fprintf(dados9, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
             case 9: fprintf(dados10, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
           }*/
           t = 0;   // zera o tempo (em horas)
           dia++;  // mais um dia
           //Nc = Nc / Df; //Diluicao
           //Nd = Nd / Df;
         }
       }// if t > 3
     } // while dia
   } // for i

  fclose(dados1);fclose(dados2);fclose(dados3);fclose(dados4);fclose(dados5);
  fclose(dados6);fclose(dados7);fclose(dados8);fclose(dados9);fclose(dados10);
  return 0;
}

/*
double f1(double Nc, double Nd){
  return gammaH*Nc*(1-(Nc+Nd)/K)*((Nc)/c - b);
}

double g1(double Nc, double Nd){
  return (1-a)*gammaH*Nd*(1-(Nc+Nd)/K)*((Nc)/c - b);
}*/

double f1(double Nc, double Nd){
  return Nc*(1+a11*Nc+a12*Nd+1-(Nc+Nd)/K)-ni;
}

double g1(double Nc, double Nd){
  return Nd*(1+a21*Nc+a22*Nd+1-(Nc+Nd)/K)-ni;
}
