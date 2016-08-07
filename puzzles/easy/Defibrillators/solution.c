#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

void char_repl(char* orig, char repl, char with);

/**
 * !!This solution is unfinished!!
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int main()
{
    // get inputs
    char LON[50];
    scanf("%s", LON); fgetc(stdin);
    char LAT[50];
    scanf("%s", LAT); fgetc(stdin);
    int N;
    scanf("%d", &N); fgetc(stdin);
    char DEFIB[256][256];
    for (int i = 0; i < N; i++) {
        fgets(DEFIB[i],256,stdin);
    }

    fprintf(stderr, "%s\n", DEFIB[0]);
    fprintf(stderr, "%d\n", N);
    
    // user position: replace ',' with '.' and convert it to float
    char_repl(LON, ',', '.');
    char_repl(LAT, ',', '.');
    float lonUser = atof(LON);
    float latUser = atof(LAT);
    
    
    char* currentDefib;
    float lonDefib[5];
    float latDefib[5];
    
    for (int i = 0; i < N; i++) {
        char temp[N][256];
        int j = 0;
        
        currentDefib = strtok(DEFIB[i], ";");
        while (currentDefib != NULL){
            strcpy(temp[j], currentDefib);
            currentDefib = strtok(NULL, ";");
            j++;
        }
        
        char_repl(temp[3], ',', '.');
        lonDefib[i] = atof(temp[3]);
        char_repl(temp[4], ',', '.');
        latDefib[i] = atof(temp[4]);
        
    }
    
    
    
//    fprintf(stderr, "%s\n", test[4]);
    
    // Write an action using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("answer\n");

    return 0;
}

void char_repl(char* orig, char repl, char with)
{
    char *ret;
    
    ret = strchr(orig, repl);
    memset(ret,with,1);
}
