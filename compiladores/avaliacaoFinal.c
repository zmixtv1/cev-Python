#include <stdio.h>
#include stdio.h
#include string.h

#define MAX_SIZE 100

// Define constants for associativity
#define ESQUERDA 1
#define DIREITA 2

// Declaração da pilha
typedef struct _Pilha
{
    char pilha[MAX_SIZE];
    int topo;
} Pilha;

// Função para inicializar a pilha
void inicializarPilha(Pilha *pilha)
{
    pilha->topo = 0;
}

// Função para verificar se a pilha está vazia
int pilhaVazia(Pilha *pilha)
{
    return pilha->topo == 0;
}

// Função para empilhar um elemento na pilha
void empilhar(Pilha *pilha, char elemento)
{
    if (pilha->topo >= MAX_SIZE)
    {
        printf("Erro: Pilha cheia!\n");
        return;
    }

    pilha->pilha[pilha->topo] = elemento;
    pilha->topo++;
}

// Função para desempilhar um elemento da pilha
char desempilhar(Pilha *pilha)
{
    if (pilhaVazia(pilha))
    {
        printf("Erro: Pilha vazia!\n");
        return '\0';
    }

    pilha->topo--;
    return pilha->pilha[pilha->topo];
}

// Função para verificar a precedência de um operador
int precedenciaOperador(char operador)
{
    switch (operador)
    {
    case '^':
        return 4;
    case '*':
    case '/':
        return 3;
    case '+':
    case '-':
        return 2;
    case '(':
    case ')':
        return 1;
    default:
        return 0;
    }
}

// Função para verificar a associatividade de um operador
int associatividadeOperador(char operador)
{
    switch (operador)
    {
    case '^':
        return DIREITA;
    case '*':
    case '/':
        return ESQUERDA;
    case '+':
    case '-':
        return ESQUERDA;
    default:
        return DIREITA;
    }
}

// Função para converter expressão infixa para pós-fixa
char *converterInfixaParaPosfixa(char expressaoInfixa[])
{
    Pilha pilha;
    inicializarPilha(&pilha);

    char expressaoPosfixa[MAX_SIZE];
    int i = 0, j = 0;

    while (expressaoInfixa[i] != '\0')
    {
        char caractereAtual = expressaoInfixa[i];

        if (caractereAtual >= 'a' && caractereAtual <= 'z' || caractereAtual >= 'A' && caractereAtual <= 'Z')
        {
            // Operando
            expressaoPosfixa[j++] = caractereAtual;
        }
        else if (caractereAtual == '(')
        {
            // Parêntese de abertura
            empilhar(&pilha, caractereAtual);
        }
        else if (caractereAtual == ')')
        {
            // Parêntese de fechamento
            while (!pilhaVazia(&pilha) && desempilhar(&pilha) != '(')
            {
                expressaoPosfixa[j++] = desempilhar(&pilha);
            }

            if (pilhaVazia(&pilha))
            {
                printf("Erro: Parênteses não balanceados!\n");
                return NULL;
            }
        }
        else if (caractereAtual == '+' || caractereAtual == '-' || caractereAtual == '*' || caractereAtual == '/' || caractereAtual == '^')
        {
            // Operador
            while (!pilhaVazia(&pilha) && precedenciaOperador(desempilhar(&pilha)) >= precedenciaOperador(caractereAtual) && associatividadeOperador(desempilhar(&pilha)) != DIREITA)
            {
                expressaoPosfixa[j++] = desempilhar(&pilha);
            }

            empilhar(&pilha, caractereAtual);
        }

        i++;
    }

    // Desempilhar os operadores restantes na pilha
    while (!pilhaVazia(&pilha))
    {
        expressaoPosfixa[j++] = desempilhar(&pilha);
    }

    expressaoPosfixa[j] = '\0'; // Adicionar terminador de string

    return expressaoPosfixa;
}

int main()
{
    char expressaoInfixa[MAX_SIZE];

    printf("Digite a expressão infixa: ");
    gets(expressaoInfixa);

    char *expressaoPosfixa = converterInfixaParaPosfixa(expressaoInfixa);

    if (expressaoPosfixa != NULL)
    {
        printf("Expressão pós-fixa: %s\n", expressaoPosfixa);
    }

    return 0;
}
