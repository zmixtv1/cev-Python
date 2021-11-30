
#include <stdio.h>
#include <stdlib.h>      
#include <ctype.h>     /* para a função isdigit(char ) */
#include <string.h>

#define tam 100

/* é declarado como variavel global, porque a pilha []
* é usada por mais de uma função */

char pilha[tam];
int top = -1;

/*definir a variavel topo(top) -> que acessa o elemento posicionado no topo da pilha*/

/* definir a função de empilhar */
/*push() -> empilhar* -> insere um novo elemento no topo da pilha */

void empilha(char item)
{
	if(top >= tam-1)
	{
		printf("\nPilha lotada.");
	}
	else
	{
		top += 1;
		pilha[top] = item;
	}
}

/*operação pop, que vai remover um elemento do topo da pilha*/
char desempilha()
{
	char item ;

	if(top <0)
	{
		printf("Expressão Infixa invalida!");
		getchar();
		/* "underflow" pode ocorrer para expressões invalidas */
		/* onde os dois parenteses não combinam */
		exit(1);
	}
	else
	{
		item = pilha[top];
		top -= 1;
		return(item);
	}
}

/* define a função que é usada para determinar se algum símbolo é operador ou não
(isto é, símbolo é operando)
* Se o simbolo for operador, a funcao retornará 1, se não for retornará 0 */

int e_operador(char simbolo)
{
	if(simbolo == '^' || simbolo == '*' || simbolo == '/' || simbolo == '+' || simbolo =='-')
	{
		return 1;
	}
	else
	{
	return 0;
	}
}

/* define a função que indica precedencia de operadores.

* Nessa função,assumimos que quanto maior o valor inteiro,
* maio a precedencia */

int precedencia(char simbolo)
{
	if(simbolo == '^')/* operador do expoente, maior precedencia*/
	{
		return(3);
	}
	else if(simbolo == '*' || simbolo == '/')
	{
		return(2);
	}
	else if(simbolo == '+' || simbolo == '-')          /* menor precedencia */
	{
		return(1);
	}
	else
	{
		return(0);
	}
}

void Infixa_Posfixa(char exp_infixa[], char exp_posfixa[])
{ 
	int i, j;
	char item;
	char z;

	empilha('(');                               /* da "push" no '(' pra pilha */
	strcat(exp_infixa,")");                  /* adiciona ')' pra expressão infixa */

	i=0;
	j=0;
	item=exp_infixa[i];         /* define a variavel antes do loop*/

	while(item != '\0')        /* roda o loop até o final da expressão infixa*/
	{
		if(item == '(')
		{
			empilha(item);
		}
		else if(isdigit(item) || isalpha(item))
		{
			exp_posfixa[j] = item;              /* adiciona o simbolo do operando pra expressão posfixa */
			j++;
		}
		else if(e_operador(item) == 1)        /* o simbolo e operador */
		{
			z=desempilha();
			while(e_operador(z) == 1 && precedencia(z)>= precedencia(item))
			{
				exp_posfixa[j] = z;                  /* desempilha os operadores da alta precedencia e */
				j++;
				z = desempilha();                       /* adiciona eles pra expressão posfixa */
			}
			empilha(z);
			/* because just above while loop will terminate we have
			oppped one extra item
			for which condition fails and loop terminates, so that one*/

			empilha(item);                 /* empilha o operador atual para a pilha */
		}
		else if(item == ')')         /* se o simbolo do operador for ')' entao */
		{
			z = desempilha();                   /*desempilhe e continue ate */
			while(z != '(')                /* '(' for encontrado */
			{
				exp_posfixa[j] = z;
				j++;
				z = desempilha();
			}
		}
		else
		{ /* se o simbolo atual não for nem operando nem '(' ou ')' e  tambem nao for
			operador */
			printf("\nExpressao Infixa invalida.\n");        /* simbolo invalido */
			getchar();
			exit(1);
		}
		i++;


		item = exp_infixa[i]; /* va para o proximo simbolo da expressao infixa */
	} /* while termina aqui */
	if(top>0)
	{
		printf("\nExpressao infixa invalida.\n");        /* invalido */
		getchar();
		exit(1);
	}
	if(top>0)
	{
		printf("\nExpressao infixa invalida.\n");        /* invalido */
		getchar();
		exit(1);
	}


	exp_posfixa[j] = '\0'; /* add sentinel else puts() fucntion */
	/* will print entire postfix[] array upto SIZE */

}

/* inicio da main */
int main()
{
	char infixa[tam], posfixa[tam];         /* declare infix string and postfix string */

	/* why we asked the user to enter infix expression
	* in parentheses ( )
	* What changes are required in porgram to
	* get rid of this restriction since it is not
	* in algorithm
	* */
	printf("Escreva as expressoes sem espaco:\n");
	
    printf("\nExpressao Infixa: ");
	gets(infixa);

	Infixa_Posfixa(infixa,posfixa);                   /* chamada para conversao */
	printf("Expressao Posfixa: ");
	puts(posfixa);                     /* printa a expressão posfixa */

	return 0;
}
