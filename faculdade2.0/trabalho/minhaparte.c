

#include <stdio.h>      /* Usando as bibliotecas */
#include <stdlib.h>     
#include <ctype.h>     /* para a função isdigit(char ) */
#include <string.h>     /* para funçoes de string */

#define tam 100  /* Define a variavel global */

/* é declarado como variavel global, porque a pilha []
* é usada por mais de uma função */

char pilha[tam];  /*Usando a variavel global porque muitas funções ira utiliza-las*/
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