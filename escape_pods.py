
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def bfs(self, s, t, parent):
        visited = [False] * self.ROW
        queue = [s]
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False

    def run_Ford_Fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow


def add_fake_vertices_2_graph(_srcs, _sinks, _graph):
    fake_sink = [0] * len(_graph)
    fake_sink_ids = [_sink + 1 for _sink in _sinks]
    fake_src = [float("Inf") if i in _srcs else 0 for i in range(len(_graph))]
    _graph.insert(0, fake_src)
    _graph.append(fake_sink)
    for i, _row in enumerate(_graph):
        _row.insert(0,0)
        if i in fake_sink_ids:
            _row.append(float("Inf"))
        else:
            _row.append(0)
    return _graph

def is_valid_input(_entrances, _exits, _path):
    result = [True if _ent in _exits else False for _ent in _entrances]
    if any(result) or len(_path) > 50:
        return False
    return True


def solution(entrances, exits, path):
    err_msg = "One of the parameters: entrances, exits, path is malformed"
    _is_valid_input = is_valid_input(_entrances=entrances, _exits=exits, _path=path)
    try:
        if not _is_valid_input:
            raise Exception
        graph = add_fake_vertices_2_graph(_srcs=entrances, _sinks=exits, _graph=path)
        new_source = 0
        new_sink = len(graph) - 1
        g = Graph(graph)
        return g.run_Ford_Fulkerson(source=new_source, sink=new_sink)
    except Exception as e:
        raise Exception("{}. {}".format(err_msg,e).strip(". "))


if __name__ == '__main__':
    original_graph = [
        [0, 0, 4, 6, 0, 0],
        [0, 0, 5, 2, 0, 0],
        [0, 0, 0, 0, 4, 4],
        [0, 0, 0, 0, 6, 6],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    sources = [0, 1]
    sinks = [4, 5]
    print ("The maximum possible flow is %d " % solution(entrances=sources, exits=sinks, path=original_graph))
