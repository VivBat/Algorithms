def create_column_sums(data):
    """
    data: Input matrix (a list of lists)
    returns: A matrix whose elements are the sum of the column from top row to the row of the element
    """
    N = len(data[0])   # size of array needed to store the result
    sum_matrix = [[] * N for i in range(N)]  # matrix to contain the result

    sum_matrix[0] = data[0]     # first row remains the same as the input since it is the first row

    for row in range(1, N):
        for col in range(N):
            sum_matrix[row].append(data[row][col] + sum_matrix[row - 1][col])   # adding the value of current cell in
            # the input matrix to the value of the cell above in the sum_matrix

    return sum_matrix


def create_sub_matrices(data, col_sums):
    """
    data: Entire input matrix col_sums: Matrix containing precalculated sums of the input matrix (summed along
    column, as done in create_column_sums method)
    return: Arrays containing the size, starting row index,
    starting column index,sum of the matrix, of all the possible combinations of square sub matrices of all sizes,
    provided the sum of the sub matrix falls between q1 and q2
    """
    N = len(data[0])
    sub_matrices_info = []   # to contain the result

    for size in range(1, N):  # to iterate over all sizes from 1 to N-1
        for row in range(N - size + 1):
            for col in range(N - size + 1):
                sum_ = []    # to help calculate sum of the sub matrix
                for i in range(col, col + size):   # iterating over all columns of the matrix to gather sum of each column
                    if row > 0:                    # when the row is not the first row
                        temp = col_sums[row + size - 1][i] - col_sums[row - 1][i]  # sum of the column, starting from the first row of the sub matrix to last row of the sub matrix
                        sum_.append(temp)   # stored the sum of each column of the sub matrix in the array
                    else:        # if it is the first row
                        temp1 = col_sums[row + size - 1][i]  # then there is no previous row so nothing is subtracted
                        sum_.append(temp1)

                sum_to_use = sum(sum_)     # summing up the sum of all the columns of the sub matrix to find the sub of the entire sub matrix
                if q1 <= sum_to_use <= q2:   # if the sum is between the quality value
                    sub_matrices_info.append([size, row, col, sum_to_use])  # only then the array is appended to the result

    return sub_matrices_info


def check_overlap(first_square, second_square):
    """
    first_square: A submatrix of a bigger matrix
    second_square: A submatrix of a bigger matrix
    returns: True if the submatrices overlap in the bigger matrix, else false
    """
    size1 = first_square[0]              # size of first matrix
    size2 = second_square[0]             # size of second matrix
    starting_row1 = first_square[1]      # starting row of first matrix
    starting_col1 = first_square[2]      # starting col of first matrix
    starting_row2 = second_square[1]     # starting row of second matrix
    starting_col2 = second_square[2]     # starting col of second matrix

    if starting_row1 <= starting_row2:      # if the first matrix is above the 2nd one
        flag = (starting_col1 + size1 - 1 < starting_col2) or (starting_row1 + size1 - 1 < starting_row2)
    elif starting_row1 >= starting_row2:    # if the first matrix is below the 2nd one
        flag = (starting_col2 + size2 - 1 > starting_col1) or (starting_row2 + size2 - 1 > starting_row1)
    elif starting_row1 == starting_row2:    # if both are at the same level
        if starting_col1 <= starting_col2:  # then checking if 1st one ahead of the 2nd one
            flag = (starting_col1 + size1 - 1 < starting_col2) or (starting_row1 + size1 - 1 < starting_row2)
        else:                               # 2nd one is ahead of the first
            flag = (starting_col2 + size2 - 1 > starting_col1) or (starting_row2 + size2 - 1 > starting_row1)

    return not flag


def solution(data):
    precalculated_col_sums = create_column_sums(data)                       # pre-calculated sum of each column of the input matrix
    sub_matrices_info = create_sub_matrices(data, precalculated_col_sums)   # the sub matrices that fall between the quality values

    # print(sub_matrices_info)

    sorted_sub_matrices = sorted(sub_matrices_info, key=lambda x: x[3], reverse=True)  # sorting (decreasing order) the sub matrices based on their sums

    # print(sorted_sub_matrices)

    # is_overlapped = check_overlap(sorted_sub_matrices[1], sorted_sub_matrices[3])   # to check overlap between 2 sub matrices
    # print(is_overlapped)

    differences = []                    # to contain the differences in the sums of all non overlapping sub-matrices
    size_of_sorted = len(sorted_sub_matrices)
    for i in range(size_of_sorted):
        for j in range(i + 1, size_of_sorted):
            if check_overlap(sorted_sub_matrices[i], sorted_sub_matrices[j]):  # if sub matrices overlap, skip
                continue
            else:           # if sub matrices don't overlap
                diff_ = sorted_sub_matrices[i][3] - sorted_sub_matrices[j][3]  # difference between the sums of the 2 sub matrices
                sum_ = sorted_sub_matrices[i][3] + sorted_sub_matrices[j][3]   # sum of the sums of 2 sub matrices
                differences.append([sorted_sub_matrices[i][3], sorted_sub_matrices[j][3], diff_, sum_]) # appending the sum of sub matrix 1, sum of sub matrix2, difference between their sums, sum of the sums of the 2 matrices

    # print(differences)

    sorted_diff = sorted(differences, key=lambda x: x[2], reverse=False)  # sorting the differences matrix so that the sub matrices with lowest sums are at the starting

    checking_for_same_sums = []  # to check in case there are multiple differences with the same difference value
    if len(sorted_diff) > 1:    # only when the differences array has more than 1 value
        i = 1
        flag = True
        checking_for_same_sums.append(sorted_diff[0])   # the first array in the differences is added by default
        while flag:
            if sorted_diff[i][2] == checking_for_same_sums[i - 1][2]:  # checking if the next ones have the same value
                checking_for_same_sums.append(sorted_diff[i])          # if same then added
                i += 1                                                 # increasing the index to see if the next one also has the same value
            flag = False                                               # if next one is not same then flag set to false to exit the loop

        answer_temp = sorted(checking_for_same_sums, key=lambda x: x[3], reverse=True)  # sorting the previous array based on the sums of the sub matrices so that the one with the biggest sum is at the starting
        answer = answer_temp[0]   # answer will the one at the starting
    else:   # if there is only one list in the differences list
        checking_for_same_sums.append(sorted_diff[0])   # then that is the answer
        answer = checking_for_same_sums[0]

    answer = sorted([answer[0], answer[1]])   # sorting to make answer more presentable

    print(answer[0], answer[1])   # printing the final answer


if __name__ == "__main__":
    N_in = int(input())  # number of rows (or columns) of a square matrix
    input_arr = [[]*N_in for i in range(N_in)]  # to contain the input matrix
    for i in range(N_in):
        input_arr[i] = input().split()    # filling up the input matrix

    q1, q2 = input().split()  # prescribed range of the quality
    q1 = int(q1)
    q2 = int(q2)

    # Converting str to int
    for row in input_arr:
        row[:] = map(int, row)

    # Testing data
    # q1 = 40
    # q2 = 55
    # input_arr =  [[ 12,  14,  16,  22,  13,  10],
    #         [ 10,  31,  12,  16,  15,  11],
    #         [-20,  19,  20,   5,   9,  12],
    #         [ 10,  15,  16,  16, -10,  23],
    #         [ 40,  89,  67,  30,  -5,  10],
    #         [ 20,  34, -95,  43,  18,  30]]

    # input_arr = [[1, 7, 3],
    #              [0, 6, 12],
    #              [-2, 8, 2,]]

    # input_arr = [[19, 14, 14, 19, 17],
    #              [18, 13, 12, 12, 19],
    #              [13, 13, 12, 14, 16],
    #              [20, 12, 10, 20, 11],
    #              [17, 15, 14, 17, 19]]

    # print(input_arr)
    # print(q1, q2)

    solution(input_arr)   # calling solution
