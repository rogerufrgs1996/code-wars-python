#include <stdbool.h>
#include <stdio.h>
#include <math.h>

bool is_prime(int num){
    if(num > 1){
        if(num == 2){
            return true;
        }
        else if(num%2 == 0){
            return false;
        }
        else{
            for(int i = (int)sqrt(num); i > 2; i--){
                if(num % i == 0){
                    return false;
                }
            }
        }
    }
    else{
        return false;
    }
    return true;
}
int main(){
   printf("\nresult %d", is_prime(7));
   return 0;
}
