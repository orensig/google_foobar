from collections import defaultdict

precomputed_pred_options = {
    True: [
        [[False, False], [False, True]],
        [[False, False], [True, False]],
        [[False, True], [False, False]],
        [[True, False], [False, False]]
    ],
    False: [
        [[False, False], [False, False]],
        [[False, False], [True, True]],
        [[False, True], [False, True]],
        [[False, True], [True, False]],
        [[False, True], [True, True]],
        [[True, False], [False, True]],
        [[True, False], [True, False]],
        [[True, False], [True, True]],
        [[True, True], [False, False]],
        [[True, True], [False, True]],
        [[True, True], [True, False]],
        [[True, True], [True, True]]
    ]
}


def transpose_matrix(_mat):
    _mat_T = tuple(zip(*_mat))
    return _mat_T


def conv_bool_vector_2_int(_vect):
    base_10_val = int("".join(map(lambda x: str(int(x)), _vect)),2)
    return base_10_val


def generate_possible_prev_cols(_col_set):
    ans = {}
    for _col in _col_set:
        base_10_col = conv_bool_vector_2_int(_col)
        current_col_options = []
        for j, _cell in enumerate(_col):
            if j == 0:
                current_col_options = precomputed_pred_options[_cell]
            else:
                current_col_option_candidates = []
                for _opt in precomputed_pred_options[_cell]:
                    for _prev_cell_opt in current_col_options:
                        if conv_bool_vector_2_int(_opt[0]) == conv_bool_vector_2_int(_prev_cell_opt[-1]):
                            current_candidate = _prev_cell_opt + [_opt[1]]
                            current_col_option_candidates.append(current_candidate)
                current_col_options = current_col_option_candidates
        current_col_options = [(conv_bool_vector_2_int(_iter[0]),conv_bool_vector_2_int(_iter[1])) for _iter in [zip(*_prev_col_opt) for _prev_col_opt in current_col_options]]
        ans[base_10_col] = current_col_options
    return ans


def count_num_prev_states(g):
    input_mat_T = transpose_matrix(g)
    all_possible_prev_cols = generate_possible_prev_cols(set(input_mat_T))
    prev_level_possible_columns = defaultdict(int)
    for i, _col in enumerate(input_mat_T):
        _col_base_10_val = conv_bool_vector_2_int(_col)
        current_level_possible_columns = all_possible_prev_cols[_col_base_10_val]
        next_level_possible_cols = defaultdict(int)
        if i == 0:
            for _ in current_level_possible_columns:
                next_level_possible_cols[_[1]] += 1
        else:
            for _prev_col, _prev_col_count in prev_level_possible_columns.items():
                for _cur_col in current_level_possible_columns:
                    if _prev_col == _cur_col[0]:
                        next_level_possible_cols[_cur_col[1]] += _prev_col_count
        prev_level_possible_columns = next_level_possible_cols
    return sum(prev_level_possible_columns.values())


def is_valid_input(_g):
    if any([len(_g[0]) < 3, len(_g[0]) > 50, len(_g) < 3, len(_g) > 50]):
        return False
    return True


def solution(g):
    err_msg = "The parameter g is malformed"
    _is_valid_input = is_valid_input(_g=g)
    try:
        if not _is_valid_input:
            raise Exception
        return count_num_prev_states(g)
    except Exception as e:
        raise Exception("{}. {}".format(err_msg, e).strip(". "))

if __name__ == '__main__':
    # mat_a = [
    #     [True, True, False, True, False, True, False, True, True, False],
    #     [True, True, False, False, False, False, True, True, True, False],
    #     [True, True, False, False, False, False, False, False, False, True],
    #     [False, True, False, False, False, False, True, True, False, False]
    # ]
    # mat_a = [
    #     [True, False, True],
    #     [False, True, False],
    #     [True, False, True]
    # ]
    mat_a = [
        [True, False, True, False, False, True, True, True],
        [True, False, True, False, False, False, True, False],
        [True, True, True, False, False, False, True, False],
        [True, False, True, False, False, False, True, False],
        [True, False, True, False, False, True, True, True]]
    print(count_num_prev_states(mat_a))






# class Graph:
#     def __init__(self):
#         self.graph = {}
#
#     def add_edge(self, u, v, npaths):
#         if u not in self.graph.keys():
#             self.graph[u] = {}
#             self.graph[u]["child"] = []
#             self.graph[u]["npaths"] = None
#         self.graph[u]["child"].append(v)
#         if v not in self.graph.keys():
#             self.graph[v] = {}
#             self.graph[v]["child"] = []
#             self.graph[v]["npaths"] = npaths
#         else:
#             self.graph[v]["npaths"] += npaths
#
#
#
#     def run_dfs(self, u, t):
#         if u == t:
#             return 1
#         else:
#             if not self.graph[u]["npaths"]:
#                 self.graph[u]["npaths"] = sum(self.run_dfs(c, t) for c in self.graph[u]["child"])
#             return self.graph[u]["npaths"]

