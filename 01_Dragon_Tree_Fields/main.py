import time

import numpy as np


def create_sums(data):
    """
      data: Input matrix (a list of lists)
      returns: A matrix whose element a[I][J] is the sum of all elements whose j <= J and i <= I
    """
    N = len(data[0])  # size of array needed to store the result

    sum_matrix = np.empty([N, N], int)  # an empty matrix to hold the sums
    sum_matrix[0][0] = data[0][0]       # populating the [0][0] element equal to data's [0][0]

    for row in range(N):
        for col in range(N):
            if row > 0 and col > 0:
                sum_matrix[row][col] = data[row][col] + sum_matrix[row][col-1] + sum_matrix[row-1][col] - sum_matrix[row-1][col-1]
            else:
                if row == 0 and col == 0:  # the [0][0] element of sum_matrix is already populated
                    continue
                if row == 0:
                    sum_matrix[row][col] = data[row][col] + sum_matrix[row][col-1]
                if col == 0:
                    sum_matrix[row][col] = data[row][col] + sum_matrix[row-1][col]

    return sum_matrix


def create_sub_matrices(data, sum_matrix):
    """
    data: Entire input matrix col_sums: Matrix containing precalculated sums of the input matrix (summed along
    column, as done in create_column_sums method)
    return: Arrays containing the size, starting row index,
    starting column index,sum of the matrix, of all the possible combinations of square sub matrices of all sizes,
    provided the sum of the sub matrix falls between q1 and q2
    """
    N = len(data[0])
    sub_matrices_info = []  # to contain the result
    # sub_matrices_info = np.empty([N, 5],int)

    for size in range(1, N):  # to iterate over all sizes from 1 to N-1
        for row in range(N - size + 1):
            for col in range(N - size + 1):
                sum_ = 0
                if row > 0 and col > 0:
                    sum_ = sum_matrix[row+size-1][col+size-1] - sum_matrix[row-1][col+size-1] - sum_matrix[row+size-1][col-1] + sum_matrix[row-1][col-1]
                if row == 0 and col == 0:
                    sum_ = sum_matrix[row+size-1][col+size-1]
                if col == 0:
                    sum_ = sum_matrix[row+size-1][col+size-1] - sum_matrix[row-1][col+size-1]
                if row == 0:
                    sum_ = sum_matrix[row+size-1][col+size-1] - sum_matrix[row+size-1][col-1]

                if q1 <= sum_ <= q2:  # if the sum is between the quality value
                    sub_matrices_info.append(
                        [size, row, col, sum_])  # only then the array is appended to the result

    # print(sub_matrices_info)
    return sub_matrices_info


def check_overlap(first_square, second_square):
    """
    first_square: A submatrix of a bigger matrix
    second_square: A submatrix of a bigger matrix
    returns: True if the submatrices overlap in the bigger matrix, else false
    """

    size1 = first_square[0]  # size of first matrix
    size2 = second_square[0]  # size of second matrix
    starting_row1 = first_square[1]  # starting row of first matrix
    ending_row1 = starting_row1 + size1
    starting_col1 = first_square[2]  # starting col of first matrix
    ending_col1 = starting_col1 + size1
    starting_row2 = second_square[1]  # starting row of second matrix
    ending_row2 = starting_row2 + size2
    starting_col2 = second_square[2]  # starting col of second matrix
    ending_col2 = starting_col2 + size2

    # print(f"size1: {size1}")
    # print(f"size2: {size2}")
    # print(f"starting row1: {starting_row1}")
    # print(f"ending_row1: {ending_row1}")
    # print(f"starting_col1: {starting_col1}")
    # print(f"ending_col1: {ending_col1}")
    # print(f"starting_row2: {starting_row2}")
    # print(f"ending_row2: {ending_row2}")
    # print(f"starting_col2: {starting_col2}")
    # print(f"ending_col2: {ending_col2}")

    if starting_row1 <= starting_row2 <= ending_row1:
        if starting_col1 < ending_col2 < ending_col1 or starting_col1 < starting_col2 < ending_col1:
            flag = True
        else:
            flag = False
    if starting_row2 <= starting_row1 <= ending_row2:
        if starting_col2 < ending_col1 < ending_col2 or starting_col2 < starting_col1 < ending_col2:
            flag = True
        else:
            flag = False

    else:
        flag = False

    return  flag


def solution(data):
    t1_creating_col_sums = time.time()
    precalculated_sums = create_sums(data)  # pre-calculated sum of each column of the input matrix
    t2_creating_col_sums = time.time()

    # print(f"Precalculated col sums: {precalculated_col_sums}")

    t1_creating_sub_matrices = time.time()
    sub_matrices_info = create_sub_matrices(data,
                                            precalculated_sums)  # the sub matrices that fall between the quality values
    t2_creating_sub_matrices = time.time()

    # print(f"submatrices: {sub_matrices_info}")

    t1_time_to_sort_submatrices = time.time()
    sorted_sub_matrices = sorted(sub_matrices_info, key=lambda x: x[3],
                                 reverse=True)  # sorting (decreasing order) the sub matrices based on their sums
    t2_time_to_sort_submatrices = time.time()

    # print(f"sorted submatrices: {sorted_sub_matrices}")

    # is_overlapped = check_overlap(sorted_sub_matrices[2], sorted_sub_matrices[3])   # to check overlap between 2 sub matrices
    # print(is_overlapped)

    t1_time_to_find_differences_of_non_overlapped_matrices = time.time()
    differences = []  # to contain the differences in the sums of all non overlapping sub-matrices
    size_of_sorted = len(sorted_sub_matrices)
    for i in range(size_of_sorted):
        for j in range(i + 1, size_of_sorted):
            if check_overlap(sorted_sub_matrices[i], sorted_sub_matrices[j]):  # if sub matrices overlap, skip
                continue
            else:  # if sub matrices don't overlap
                if j > i+1:
                    if sorted_sub_matrices[i][3] - sorted_sub_matrices[j-1][3] != sorted_sub_matrices[i][3] - sorted_sub_matrices[j][3]:  # if the next one doesn't have the same difference then no point in checking all the elements afterwards
                        break
                diff_ = sorted_sub_matrices[i][3] - sorted_sub_matrices[j][3]  # difference between the sums of the 2 sub matrices
                sum_ = sorted_sub_matrices[i][3] + sorted_sub_matrices[j][3]  # sum of the sums of 2 sub matrices
                differences.append([sorted_sub_matrices[i][3], sorted_sub_matrices[j][3], diff_,
                                    sum_])  # appending the sum of sub matrix 1, sum of sub matrix2, difference between their sums, sum of the sums of the 2 matrices

    t2_time_to_find_differences_of_non_overlapped_matrices = time.time()

    # print(f"differences: {differences}")

    t1_sorted_differeces = time.time()
    sorted_diff = sorted(differences, key=lambda x: x[2],
                         reverse=False)  # sorting the differences matrix so that the sub matrices with lowest sums are at the starting
    t2_sorted_differeces = time.time()

    # print(f"sorted differneces: {sorted_diff}")

    t1_checking_for_same_sums = time.time()
    checking_for_same_sums = []  # to check in case there are multiple differences with the same difference value
    if len(sorted_diff) > 1:  # only when the differences array has more than 1 value
        i = 1
        flag = True
        checking_for_same_sums.append(sorted_diff[0])  # the first array in the differences is added by default
        while flag:
            if sorted_diff[i][2] == checking_for_same_sums[i - 1][2]:  # checking if the next ones have the same value
                checking_for_same_sums.append(sorted_diff[i])  # if same then added
                i += 1  # increasing the index to see if the next one also has the same value
            flag = False  # if next one is not same then flag set to false to exit the loop

        answer_temp = sorted(checking_for_same_sums, key=lambda x: x[3],
                             reverse=True)  # sorting the previous array based on the sums of the sub matrices so that the one with the biggest sum is at the starting
        answer = answer_temp[0]  # answer will the one at the starting
    else:  # if there is only one list in the differences list
        checking_for_same_sums.append(sorted_diff[0])  # then that is the answer
        answer = checking_for_same_sums[0]
    t2_checking_for_same_sums = time.time()

    # print(f"Time to create col sums: {t2_creating_col_sums - t1_creating_col_sums}")
    # print(f"Time to create sub matrices: {t2_creating_sub_matrices - t1_creating_sub_matrices}")
    # print(f"Time to sort submatrices: {t2_time_to_sort_submatrices - t1_time_to_sort_submatrices}")
    # print(f"Time to find differences: {t2_time_to_find_differences_of_non_overlapped_matrices - t1_time_to_find_differences_of_non_overlapped_matrices}")
    # print(f"Time to sort the differences: {t2_sorted_differeces - t1_sorted_differeces}")
    # print(f"Time to check same sums: {t2_checking_for_same_sums-t1_checking_for_same_sums}")

    answer = sorted([answer[0], answer[1]])  # sorting to make answer more presentable

    print(answer[0], answer[1])  # printing the final answer


if __name__ == "__main__":
    N_in = int(input())  # number of rows (or columns) of a square matrix

    input_arr = np.empty(shape=[0, N_in])

    for i in range(N_in):
        input_arr = np.append(input_arr, [input().split()], axis=0)

    q1, q2 = input().split()  # prescribed range of the quality
    q1 = int(q1)
    q2 = int(q2)

    input_arr = input_arr.astype(int)

    # # Testing data
    # q1 = 70
    # q2 = 85
    # input_arr =  np.array([[ 12,  14,  16,  22,  13,  10],
    #         [ 10,  31,  12,  16,  15,  11],
    #         [-20,  19,  20,   5,   9,  12],
    #         [ 10,  15,  16,  16, -10,  23],
    #         [ 40,  89,  67,  30,  -5,  10],
    #         [ 20,  34, -95,  43,  18,  30]])

    # input_arr = np.array([[-1, 2, 0],
    #              [0, 1, -2],
    #              [3, 1, 2,]])

    # input_arr = [[19, 14, 14, 19, 17],
    #              [18, 13, 12, 12, 19],
    #              [13, 13, 12, 14, 16],
    #              [20, 12, 10, 20, 11],
    #              [17, 15, 14, 17, 19]]

    # # print(input_arr)
    # # print(q1, q2)

    solution(input_arr)  # calling solution
