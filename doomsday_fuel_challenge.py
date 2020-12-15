from fractions import Fraction
import numpy as np


def is_square_mat(matrix):
    return len(matrix[0]) == len(matrix)


def is_valid_input(matrix):
    ans = True
    if len(matrix) > 10 or not is_square_mat(matrix=matrix):
        ans = False
    for _row in matrix:
        if len(_row) > 10:
            ans = False
        has_negative = [_val < 0 for _val in _row]
        if True in has_negative:
            ans = False
    return ans


def get_filtered_matrix(matrix, relevant_rows, relevant_cols):
    filtered_matrix = [[_lst_iter[j] for j in relevant_cols] for _lst_iter in [matrix[i] for i in relevant_rows]]
    return filtered_matrix


def get_absorb_and_trans_states(matrix):
    absorb_states = []
    trans_states = []
    for i, _lst_iter in enumerate(matrix):
        if sum(_lst_iter) == 0:
            absorb_states.append(i)
        else:
            trans_states.append(i)
    return absorb_states,trans_states


def mat_subtract(mat1, mat2):
    ans_mat = []
    for _row, _ in enumerate(mat2):
        ans_mat.append([])
        for _col, __ in enumerate(_):
            ans_mat[_row].append(mat1[_row][_col] - __)
    return ans_mat


def solution(m):
    is_valid_in = is_valid_input(matrix=m)
    if not is_valid_in:
        raise Exception("The parameter m is malformed")
    if len(m) == 1:
        return [1,1]
    px = [[float(_)/sum(__) if sum(__) != 0 else 0 for _ in __] for __ in m]
    absorb_states, trans_states = get_absorb_and_trans_states(matrix=m)
    r_matrix = get_filtered_matrix(matrix=px, relevant_rows=trans_states, relevant_cols=absorb_states)
    q_matrix = get_filtered_matrix(matrix=px, relevant_rows=trans_states, relevant_cols=trans_states)
    q_matrix_n = len(q_matrix)
    ident_q_matrix = np.identity(n=q_matrix_n)
    ident_minus_q_matrix = mat_subtract(mat1=ident_q_matrix, mat2=q_matrix)
    n_matrix = np.linalg.inv(a=np.asmatrix(ident_minus_q_matrix, dtype="float")).tolist()
    m_matrix = np.matmul(n_matrix,r_matrix)
    terminal_states_fract_prob_list = [Fraction(_prob).limit_denominator() for _prob in m_matrix[0]]
    terminal_states_denoms = [_fract.denominator for _fract in terminal_states_fract_prob_list]
    lcm = np.lcm.reduce([dn for dn in terminal_states_denoms])
    ans = [int(fr.numerator * lcm / fr.denominator) for fr in terminal_states_fract_prob_list]
    ans.append(lcm)
    ans = np.array(ans).astype(np.int32).tolist()
    return ans


if __name__ == '__main__':
     # x = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
     # x = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
     # x = [[1, 1, 1, 1, 1,],  [0, 0, 0, 0, 0,], [1, 1, 1, 1, 1,], [0, 0, 0, 0, 0,], [1, 1, 1, 1, 1,]]
     # x = [[0]]
     x=[]
     vals = solution(m=x)
     print(vals)



