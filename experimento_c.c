#include <stdio.h>
#include <stdlib.h>

void llenar_arreglo(int list[], int num_entradas) {
    for (int i = 0; i < num_entradas; i++) {
        list[i] = rand() % 100 + 1;
    }
}

void imprimir_arreglo(int list[], int num_entradas) {
    for (int i = 0; i < num_entradas; i++) {
        printf("%d ", list[i]);
    }
    printf("\n");
}

void ordenar_arreglo(int list[], int num_entradas) {
    for (int i = 0; i < num_entradas - 1; i++) {
        for (int j = 0; j < num_entradas - i - 1; j++) {

            if (list[j] > list[j + 1]) {
                int temporal = list[j];
                list[j] = list[j + 1];
                list[j + 1] = temporal;
            }

        }
    }
}

int main() {
    int num_entradas = 10000;
   // printf("Numero de elementos a reorganizar: ");
   // scanf("%d", &num_entradas);

    int list[num_entradas];

    llenar_arreglo(list, num_entradas);

    //imprimir_arreglo(list, num_entradas);

    ordenar_arreglo(list, num_entradas);

    //imprimir_arreglo(list, num_entradas);

;

    return 0;
}
