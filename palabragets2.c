#include <stdio.h>

int main(){
    char palabra[20];
    printf("Ingrese una palabra: ");
    fgets(palabra, 20, stdin);
    printf("%s\n", palabra);
    return 0;
}