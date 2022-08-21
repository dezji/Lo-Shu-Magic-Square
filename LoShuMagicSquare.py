# Author Name: Deziallia Morris
# Purpose: Test different inputs to qualify as a magic square

ROWS = 4
COLUMNS = 4


def main():

    numbers = [[4, 14, 15, 1],
               [9, 7, 6, 12],
               [5, 11, 10, 8],
               [16, 2, 3, 13]]
    print(f"Is {numbers} a square?\n")

    magic_square_test(numbers)


def magic_square_test(numbers_list):

    # rows
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0

    # columns
    sum5 = 0
    sum6 = 0
    sum7 = 0
    sum8 = 0

    # diagonals
    sum9 = 0
    sum10 = 0

    for r in range(ROWS):
        sum1 += numbers_list[0][r]
        sum2 += numbers_list[1][r]
        sum3 += numbers_list[2][r]
        sum4 += numbers_list[3][r]

        sum5 += numbers_list[r][0]
        sum6 += numbers_list[r][1]
        sum7 += numbers_list[r][2]
        sum8 += numbers_list[r][3]

    for r in range(ROWS):
        sum9 += numbers_list[r][r]

    for r in range(ROWS):
        sum10 += numbers_list[r][ROWS - r - 1]

    if sum1 == sum2 == sum3 == sum4 == sum5 == sum6 == sum7 == sum8 == sum9 == sum10:
        print(True)
    else:
        print(False)


main()
