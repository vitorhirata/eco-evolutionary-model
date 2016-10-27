#include<stdio.h>
#include<math.h>

#define K 140000
#define a 0.000001
#define b 0.1
#define c 3
#define d 1
#define EPS 0.0001
#define Df 667
#define ni 8000

double f1(double Nc, double Nd);
double g1(double Nc, double Nd);

int main(){
  int i,dia;
  double k1C, k2C, k3C, k4C, k1D, k2D, k3D, k4D, h, Ncrit;
  double Nc, Nd, t;
  FILE *dados1, *dados2, *dados3, *dados4, *dados5,*dados6, *dados7, *dados8, *dados9, *dados10;

  dados1 = fopen("txt/modelo-carla1.txt", "w");
  dados2 = fopen("txt/modelo-carla2.txt", "w");
  dados3 = fopen("txt/modelo-carla3.txt", "w");
  dados4 = fopen("txt/modelo-carla4.txt", "w");
  dados5 = fopen("txt/modelo-carla5.txt", "w");
  dados6 = fopen("txt/modelo-carla6.txt", "w");
  dados7 = fopen("txt/modelo-carla7.txt", "w");
  dados8 = fopen("txt/modelo-carla8.txt", "w");
  dados9 = fopen("txt/modelo-carla9.txt", "w");
  dados10 = fopen("txt/modelo-carla10.txt", "w");

  h = 0.0005;
  Ncrit = 276;

  for(i=0;i<10;i++){
    dia=0;
    t=0;
    switch (i) {
      case 0: Nc=135;Nd=8865; fprintf(dados1, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 1: Nc=200;Nd=800; fprintf(dados2, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 2: Nc=240;Nd=60; fprintf(dados3, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 3: Nc=250;Nd=0; fprintf(dados4, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 4: Nc=600;Nd=0; fprintf(dados5, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 5: Nc=480;Nd=120; fprintf(dados6, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 6: Nc=600;Nd=400; fprintf(dados7, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 7: Nc=500;Nd=9500; fprintf(dados8, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 8: Nc=2000;Nd=38000; fprintf(dados9, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
      case 9: Nc=46000;Nd=69000; fprintf(dados10, "%f  %f\n", Nc+Nd, Nc/(Nc+Nd)); break;
    }

  //  Nc = Nc / Df;
  //  Nd = Nd / Df;
    dia++;
    while(dia < 40){
      t = t + h;
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

      if(Nc < 0 || Nd < 0)
        break;

      if(fabs(t-23.5) < EPS){ // Se tiver no tempo 23.5 horas
        switch (i) {
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
        t = 0;
        dia++;
      //  Nc = Nc / Df;
      //  Nd = Nd / Df;
      }
    } // while dia
  } // for i


  fclose(dados1);fclose(dados2);fclose(dados3);fclose(dados4);fclose(dados5);
  fclose(dados6);fclose(dados7);fclose(dados8);fclose(dados9);fclose(dados10);
  return 0;
}


double f1(double Nc, double Nd){
  return Nc * (a*Nc + b*Nd + 1 - (Nc+Nd)/K) - ni*Nc/(Nc+Nd);
}

double g1(double Nc, double Nd){
  return  Nd * (c*Nc + d*Nd + 1 - (Nc+Nd)/K) - ni*Nd/(Nc+Nd);
}
