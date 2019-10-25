 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
void cesar_crypt (int decallage, char *texte)
{
 
    int i;
    for(i=0 ; i<strlen(texte) ; i++)
        /* Si le caractere est une minuscule */
        if ('a' <= texte[i] && texte[i] <= 'z')
            texte[i] = 'a' + ((texte[i] - 'a') + decallage)%26;
        else
            /* Si le caractere est une majuscule */
            if ('A' <= texte[i] && texte[i] <= 'Z')
                texte[i] = 'A' + ((texte[i] - 'A') + decallage)%26;
            else
                /* Si le caractere est un chiffre */
                if ('0' <= texte[i] && texte[i] <= '9')
                    texte[i] = '0' + ((texte[i] - '0') + decallage)%9;
                
}
 
 
int main()
{
    char Test[] = "Guillaume02";
 
    cesar_crypt(13, Test);
 
    printf("%s\n\n", Test);
 
    return EXIT_SUCCESS;
}