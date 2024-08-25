#include <stdio.h>
#include <string.h>
int main() {
    char* frase = "salsa";
    int i;
    for (int i = 0; i < strlen(frase); i++) {
        if (frase[i] == 's')
            printf("Está la S");
    };
    return 0;
}