#include <stdio.h>
#include <string.h>
#include <ctype.h>  // Para a função isalpha

#define MAX_SIZE 100

// Define constants for associativity
#define ESQUERDA 1
#define DIREITA 2

// Declaração da pilha
typedef struct _Pilha {
    char pilha[MAX_SIZE];
    int topo;
} Pilha;

// Função para inicializar a pilha
void inicializarPilha(Pilha *pilha) {
    pilha->topo = 0;
}

// Função para verificar se a pilha está vazia
int pilhaVazia(Pilha *pilha) {
    return pilha->topo == 0;
}

// Função para empilhar um elemento na pilha
void empilhar(Pilha *pilha, char elemento) {
    if (pilha->topo >= MAX_SIZE) {
        printf("Erro: Pilha cheia!\n");
        return;
    }

    pilha->pilha[pilha->topo] = elemento;
    pilha->topo++;
}

// Função para desempilhar um elemento da pilha
char desempilhar(Pilha *pilha) {
    if (pilhaVazia(pilha)) {
        printf("Erro: Pilha vazia!\n");
        return '\0';
    }

    pilha->topo--;
    return pilha->pilha[pilha->topo];
}

// Função para verificar a precedência de um operador
int precedenciaOperador(char operador) {
    switch (operador) {
        case '^':
            return 4;
        case '*':
        case '/':
            return 3;
        case '+':
        case '-':
            return 2;
        default:
            return 0;
    }
}

// Função para verificar a associatividade de um operador
int associatividadeOperador(char operador) {
    switch (operador) {
        case '^':
            return DIREITA;
        case '*':
        case '/':
        case '+':
        case '-':
            return ESQUERDA;
        default:
            return DIREITA;
    }
}

// Função para converter expressão infixa para pós-fixa
char *converterInfixaParaPosfixa(char expressaoInfixa[]) {
    static char expressaoPosfixa[MAX_SIZE];  // Usando static para retornar a string
    Pilha pilha;
    inicializarPilha(&pilha);

    int i = 0, j = 0;

    while (expressaoInfixa[i] != '\0') {
        char caractereAtual = expressaoInfixa[i];

        if (isalpha(caractereAtual)) {
            // Operando
            expressaoPosfixa[j++] = caractereAtual;
        } else if (caractereAtual == '(') {
            // Parêntese de abertura
            empilhar(&pilha, caractereAtual);
        } else if (caractereAtual == ')') {
            // Parêntese de fechamento
            char topo;
            while ((topo = desempilhar(&pilha)) != '(') {
                if (pilhaVazia(&pilha)) {
                    printf("Erro: Parênteses não balanceados!\n");
                    return NULL;
                }
                expressaoPosfixa[j++] = topo;
            }
        } else if (caractereAtual == '+' || caractereAtual == '-' || caractereAtual == '*' || caractereAtual == '/' || caractereAtual == '^') {
            // Operador
            while (!pilhaVazia(&pilha) && precedenciaOperador(pilha.pilha[pilha.topo - 1]) >= precedenciaOperador(caractereAtual) && associatividadeOperador(pilha.pilha[pilha.topo - 1]) == ESQUERDA) {
                expressaoPosfixa[j++] = desempilhar(&pilha);
            }

            empilhar(&pilha, caractereAtual);
        }

        i++;
    }

    // Desempilhar os operadores restantes na pilha
    while (!pilhaVazia(&pilha)) {
        expressaoPosfixa[j++] = desempilhar(&pilha);
    }

    expressaoPosfixa[j] = '\0'; // Adicionar terminador de string

    return expressaoPosfixa;
}

int main() {
    char expressaoInfixa[MAX_SIZE];

    printf("Digite a expressão infixa: ");
    fgets(expressaoInfixa, MAX_SIZE, stdin);
    // Remover o caractere de nova linha, se presente
    expressaoInfixa[strcspn(expressaoInfixa, "\n")] = '\0';

    char *expressaoPosfixa = converterInfixaParaPosfixa(expressaoInfixa);

    if (expressaoPosfixa != NULL) {
        printf("Expressão pós-fixa: %s\n", expressaoPosfixa);
    }

    return 0;
}
