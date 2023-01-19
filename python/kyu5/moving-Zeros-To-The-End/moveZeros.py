array = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]


def move_zeros(array):
    b = [0]
    for x in array:
        if x == 0:
            array.remove(x)
            array.extend(b)
    return array


print(move_zeros(array))
