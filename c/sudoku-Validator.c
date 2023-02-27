#include <stdbool.h>

bool validateLine(int board[9][9]){
    for(int i = 0; i < 9; i++)
    {
        for (int j = 0; j< 8; j++)
        {
            for(int z = 1 + j; z < 9 ; z++)
            {
                if(board[i][j] == board[i][z] || board[i][j] == 0 || board[i][z]==0)
                {
                    return false;
                }
            }
        }
    }
    return true;
}
bool validateColumn(int board[9][9]){
    for(int j = 0; j < 9; j++)
    {
        for (int i = 0; i< 8; i++)
        {
            for(int z = i+1; z < 9 ; z++)
            {
                if(board[i][j] == board[z][j])
                {
                    return false;
                }
            }
        }
    }
    return true;
}
bool testBlock(int block[9]){
    for (int j = 0; j< 8; j++)
    {
        for(int z = 1 + j; z < 9 ; z++)
        {
            if(block[j] == block[z])
            {
                return false;
            }
        }
    }
        return true;
}
bool validateBlock(int board[9][9]){
    for(int i = 0; i < 9; i = i +3)
    {
        for (int j = 0; j< 9; j= j + 3)
        {
            int block[9] = {};
            int sum = 0;
            int count = 0;
            for(int x = 0 ; x < 3 ; x++)
            {
                for(int y = 0; y < 3; y++)
                {
                    block[count] = board[i + x][j+y];
                    sum =sum + board[i + x][j+y];
                    count ++;
                }
            }
            if(sum != 45 || testBlock(block)== false){
                return false;
            }
        }
    }
    return true;
}
bool validateSudoku(int board[9][9]){
    if(validateBlock(board)==true && validateColumn(board)==true && validateLine(board) == true){
        return true;
    }
    else{
        return false;
    }
}
int main(){
    int board[9][9] ={
	{1,2,3,4,5,6,7,8,9},
	{2,3,4,5,6,7,8,9,1},
	{3,4,5,6,7,8,9,1,2},
	{4,5,6,7,8,9,1,2,3},
	{5,6,7,8,9,1,2,3,4},
	{6,7,8,9,1,2,3,4,5},
	{7,8,9,1,2,3,4,5,6},
	{8,9,1,2,3,4,5,6,7},
	{9,1,2,3,4,5,6,7,8}};
    validateSudoku(board);
return 0;
}
