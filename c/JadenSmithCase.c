#include <stdio.h>
#


char *to_jaden_case (char *jaden_case, const char *string)
{   int upper;
    char strn[] = *string;
    for(int i =0; strn[i]!='\0'; i++){
        if(i==0 || upper == 1;){
            strn[i] = toupper(strn[i]));
            upper = 0;
        }
        else if(strn == ' '){
            upper = 1;
        }
    }
	*jaden_case = strn;
	return jaden_case;
}

int main(){
char frase[MAXTAM];
printf("digite a frase-> ");
gets(frase);
int primeira = 1;
for(int i = 0; frase[i] != '\0'; i++){
    if (primeira ==1){
       frase[i] = toupper(frase[i]);
       primeira = 0;
    }
    else if(frase[i] == ' '){
        primeira = 1;
    }
}
printf(frase);

return 0;

}
