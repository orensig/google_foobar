
class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_vertex(self, vertex, num_iterations):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = (num_iterations, [])

    def add_edge(self, edge):
        (_vertex1, _vertex2) = tuple(edge)
        self.graph_dict[_vertex1][1].append(_vertex2)

    def get_vertices(self):
        return list(self.graph_dict.keys())

    def find_edges(self):
        edge_name = []
        for _vertex in self.graph_dict:
            for _next_vertex in self.graph_dict[_vertex]:
                if {_next_vertex, _vertex} not in edge_name:
                    edge_name.append({_vertex, _next_vertex})
        return edge_name

    def build_graph(self, _max_m, _max_f):
        i = 1
        list_vertices = self.get_vertices()
        m_list_max = max(list(zip(*list_vertices)[0]))
        f_list_max = max(list(zip(*list_vertices)[1]))
        while i <= max(_max_m, _max_f)+1:
            list_vertices = [k for k,v in self.graph_dict.items() if v[1] == []]
            m_list_max = max(list(zip(*list_vertices)[0]))
            f_list_max = max(list(zip(*list_vertices)[1]))
            for _vertex in list_vertices:
                (_m, _f) = tuple(_vertex)
                v1_2_add = (_m + _f, _f)
                if v1_2_add not in list_vertices:
                    self.add_vertex(v1_2_add, i)
                    e1_2_add = (_vertex, v1_2_add)
                    self.add_edge(edge=e1_2_add)
                v2_2_add = (_m, _f + _m)
                if v2_2_add not in list_vertices:
                    self.add_vertex(v2_2_add, i)
                    e2_2_add = (_vertex, v2_2_add)
                    self.add_edge(edge=e2_2_add)
                if (_max_m, _max_f) in [v1_2_add, v2_2_add] or (_max_f, _max_m) in [v1_2_add, v2_2_add]:
                    return str(i)
            i += 1
        print(m_list_max, f_list_max)
        return "impossible"


def count_iterations(_m, _f):
    i = 0
    next_options_stack = (_m, _f)
    while True:
        current_m = next_options_stack[0]
        current_f = next_options_stack[1]
        if 1 in [current_m,current_f]:
            return str(i + max(current_m,current_f) - 1)
        elif max(current_m,current_f) % min(current_m,current_f) == 0:
            return "impossible"
        else:
            div_max_min = max(current_m,current_f)//min(current_m,current_f)
            next_options_stack = (max(current_m,current_f) % min(current_m,current_f), min(current_m,current_f))
        i += div_max_min


def is_valid_input(_x, _y):
    if not isinstance(_x, str) or not isinstance(_y, str):
        return False, None, None
    try:
        _x = long(_x)
        _y = long(_y)
        if not 0 < _x <= 10 ** 50 or not 0 < _y <= 10 ** 50:
            return False, None, None
    except Exception as e:
        return False, None, None
    return True, _x, _y


def solution(x, y):
    err_msg = "One of the parameters x,y is malformed (or both)"
    try:
        _is_valid_input, x, y = is_valid_input(_x=x, _y=y)
        if not _is_valid_input:
            raise Exception
        return count_iterations(_m=x, _f=y)
    except Exception as e:
        raise Exception("{}. {}".format(err_msg,e).strip(". "))



if __name__ == '__main__':
    # "M,F"
    # graph = Graph(graph_dict={(1, 1): (0, [])})
    # print(graph.build_graph(100,101))
    # # print(graph.__dict__)
    # # print("{}".format(graph.graph_dict))
    # graph.graph_dict = OrderedDict(sorted(graph.graph_dict.items(), key=lambda tup: (tup[0][0], tup[0][1])))
    # print(graph.graph_dict)
    # # print("\n")
    # # for k,v in graph.graph_dict.items():
    # #     print("{} : {}".format(k,v))
    # print(count_iterations(4, 7))
    # print(count_iterations(7, 4))

    print(count_iterations(10**50, ((10**50)/2) + 1))