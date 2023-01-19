def valid_solution(board):
    block = []
    validation = True  # it's true until there is evidence of the otherwise
    column = [0, 0, 0]
    for y in range(0, 7, 3):  # y represent the columns 3x3
        if not validation:
            break
        else:
            for i, j in zip(range(0, 7, 3), range(3, 10, 3)):  # i e j select the elements of board in 3x3
                if not validation:
                    break
                else:
                    for line in board[i:j]:
                        if sum(line) != 45:  # checks if line has the nine digits
                            validation = False
                            break
                        else:  # saves the sums of 3 columns
                            column = [column[0] + line[y], column[1] + line[y + 1], column[2] + line[y + 2]]
                            block.append(sum(line[y:y + 3]))  # saves the sum of the block elements
                    else:
                        if sum(block) != 45:  # checks if block has the nine digits
                            validation = False
                        else:
                            block.clear()  # empty the variable to check the next block
            else:
                if column.count(45) != 3:  # checks if the three columns has the nine digits
                    validation = False
                else:
                    column = [0, 0, 0]  # empty the variable to check the next three columns

    return validation
