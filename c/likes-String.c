
#include<string.h>
#include<stdio.h>
#include <ctype.h>
int testDuplicate(char duplicate[], char test, int count)
{
    for(int i =0; i < count; i++){
        printf("\nteste I -> %d -- duplicat[i] -> %c  test -> %c", i, duplicate[i], test);
        if(duplicate[i] == test){
            printf("\nduplicate i %c", duplicate[i] );
            printf("\ntest %c", test );
            return 1;
        }
    }
    return 0;



}
//size_t duplicate_count(const char *text) {
int main(){
    char text[] = {"99redballons99bottlesofbeeronthewall"};
    char duplicate[(int)strlen(text)/2];
    int count = 0;
    char test = '*';
    char aux = '*';
    printf("\nlen %d", strlen(text));
    for(int i =0; i < ((int)strlen(text)-1); i++){
        printf("\n------------i-> %d", i);
        if(aux != text[i]){

            for(int j = i +1; j < (int)strlen(text); j++){
                printf("\nJ-> %d---  text[i]-> %c  ee  text[j]-> %c", j, text[i], text[j]);
                test = tolower(text[i]);
                if(tolower(text[i]) == tolower(text[j]) && testDuplicate(duplicate, test, count) == 0){
                   printf("\nENTROU i-> %c",text[i]);
                   printf("\nENTROU j -> %c", text[j]);
                   duplicate[count] = tolower(text[i]);
                   count ++ ;
                   printf("\nCOUNT - > %d", count);
                   break;
                }
            }
            aux = text[i];
        }
    }
    printf("\nresposta - > %d", count);
    return 0;

}
