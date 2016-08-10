/* Implementação do algoritmo Diffie-Hellman */ 

#include<stdio.h>
#include<math.h>

int calcular(int base, int expoente, int modulo);

int main(){
	
	double g = 7, n = 11; //base e modulo
	int var, x, mod;
      
	printf("Digite o número secreto:");
	scanf("%d",&x);
	  
	mod = calcular(g,x,n);
	printf("Calculado: %d\n",mod);
	
	printf("Digite o número recebido:");
	scanf("%d",&var);
	
	mod = calcular(var,x,n);
	printf("Chave secreta: %d\n",mod);
	
	return 0;
}

int calcular(int base, int expoente, int modulo){
	int potencia = 1, contador = 0;
	
	while (contador != expoente) {
		potencia *= base;
		contador += 1;
	}
	return potencia % 11;
}
