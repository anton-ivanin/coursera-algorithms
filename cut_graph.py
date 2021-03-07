import random
import copy


def cut():

    global graph
    global vertex_number

    vertex = 0

    while vertex not in graph:
        vertex = random.randint(1, vertex_number)

    raw = graph[vertex]
    edge_count = len(raw)
    edge_num = random.randint(1, edge_count)
    cor_vertex = graph[vertex][edge_num - 1]
    cor_raw = graph[cor_vertex]

    for cur_vertex in cor_raw:
        if cur_vertex != vertex:
            raw.append(cur_vertex)

        cur_raw = graph[cur_vertex]

        while cor_vertex in cur_raw:
            cur_raw.remove(cor_vertex)
            if cur_vertex != vertex:
                cur_raw.append(vertex)

    del graph[cor_vertex]


def count_edges(graph):
    for raw in graph.values():
        return len(raw)


vertex_number = 200

graph = dict()
graph[1] = [2, 5, 6]
graph[2] = [1, 3, 5, 6]
graph[3] = [2, 4, 7, 8]
graph[4] = [3, 7, 8]
graph[5] = [1, 2, 6]
graph[6] = [1, 2, 5, 7]
graph[7] = [3, 4, 6, 8]
graph[8] = [3, 4, 7]

graph = dict()

with open("kargerMinCut.txt", "r") as file:
    for line in file:
        pos_tab = line.find("\t")
        vertex = int(line[0:pos_tab])
        graph[vertex] = list()
        line = line[pos_tab + 1:]
        while True:
            pos_tab = line.find("\t")
            if pos_tab == -1:
                break
            else:
                graph[vertex].append(int(line[0:pos_tab]))
                line = line[pos_tab + 1:]

cut_num = 0

for i in range(vertex_number * vertex_number):
    # if i % vertex_number == 0:
    print(f'iteration {i} cut_num {cut_num}')

    copy_graph = copy.deepcopy(graph)
    while len(graph) > 2:
        cut()

    edge_number = count_edges(graph)

    if cut_num == 0:
        cut_num = edge_number
    else:
        cut_num = min(cut_num, edge_number)

    graph = copy.deepcopy(copy_graph)

print(cut_num)
