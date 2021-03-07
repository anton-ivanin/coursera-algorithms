import sys
import copy

t = 0
s = 0
scc_size = 0

explored = dict()
graph = dict()
leaders = dict()
finished_time = dict()
stack = []


def complete_sample_graph5():
    global graph

    graph = dict()
    graph[1] = [2]
    graph[2] = [3, 4, 5]
    graph[3] = [6]
    graph[4] = [5, 7]
    graph[5] = [2, 6, 7]
    graph[6] = [3, 8]
    graph[7] = [8, 10]
    graph[8] = [7]
    graph[9] = [7]
    graph[10] = [9, 11]
    graph[11] = [12]
    graph[12] = [10]


def complete_sample_graph4():
    global graph

    graph = dict()
    graph[1] = [2]
    graph[2] = [3]
    graph[3] = [1, 4]
    graph[4] = [3, 6]
    graph[5] = [4]
    graph[6] = [4, 7]
    graph[7] = [8]
    graph[8] = [6]


def complete_sample_graph3():
    global graph

    graph = dict()
    graph[1] = [2]
    graph[2] = [3]
    graph[3] = [1, 4]
    graph[4] = []
    graph[5] = [4]
    graph[6] = [4, 7]
    graph[7] = [8]
    graph[8] = [6]


def complete_sample_graph2():
    global graph

    graph = dict()
    graph[1] = [2]
    graph[2] = [3, 4, 6]
    graph[3] = [1, 4]
    graph[4] = [5]
    graph[5] = [4]
    graph[6] = [5, 7]
    graph[7] = [6, 8]
    graph[8] = [5, 7]


def complete_sample_graph1():
    global graph

    graph = dict()
    graph[1] = [4]
    graph[2] = [8]
    graph[3] = [6]
    graph[4] = [7]
    graph[5] = [2]
    graph[6] = [9]
    graph[7] = [1]
    graph[8] = [5, 6]
    graph[9] = [3, 7]


def complete_sample_reversed_graph():
    global graph

    graph = dict()
    graph[1] = [4]
    graph[2] = [1]
    graph[3] = [2]
    graph[4] = [3]
    graph[5] = [4, 7]
    graph[6] = [5]
    graph[7] = [6]


def complete_graph():
    global graph
    graph = dict()
    prev_vertex = 0
    with open("SCC.txt", "r") as file:
        for line in file:
            pos_tab = line.find(" ")
            vertex = int(line[0:pos_tab])

            if vertex - prev_vertex > 1:
                for j in range(prev_vertex + 1, vertex):
                    graph[j] = list()

            prev_vertex = vertex

            if vertex not in graph:
                graph[vertex] = list()

            line = line[pos_tab + 1:]
            pos_tab = line.find(" ")
            cor_vertex = int(line[0:pos_tab])
            if vertex != cor_vertex & cor_vertex not in graph[vertex]:
                graph[vertex].append(cor_vertex)


def dfs_loop():

    global t
    global s
    global graph
    global explored
    global stack

    global leaders
    global finished_time

    t = 0
    s = 0
    n = len(graph)
    stack1 = []
    for i in range(n,0,-1):
        cur_vertex = i
        if cur_vertex not in explored:
            s = cur_vertex
        else:
            continue

        stack1.append(s)
        dfs(s)


def dfs(i, regime=0):
    global t
    global scc_size
    global graph
    global finished_time
    global leaders
    stack = [i]
    stack1 = []
    while len(stack) != 0:  # check whether there is anything in the To-Do list
        newNode = stack.pop()  # get next node to visit


        if newNode not in explored:  # update visited if this node has not been visited
            explored[newNode] = True
            stack.append(newNode)
            scc_size += 1
            if len(graph[newNode]) == 0:
                if newNode not in finished_time:
                    finished_time[newNode] = t
                    t += 1
            for neighbor in graph[newNode]:  # iterate over neighbors
                if neighbor not in explored:  # check whether neighbors were visited
                    stack.append(neighbor)
        else:
            stack1.append(newNode)
            # if newNode not in finished_time:
            #     finished_time[newNode] = t
            #     t += 1

    for newNode in stack1:
        if newNode not in finished_time:
            finished_time[newNode] = t
            t += 1

#sys.setrecursionlimit(10000)

explored = dict()

#complete_sample_graph5()
#complete_sample_reversed_graph()
complete_graph()

for item in graph:
    graph[item].sort()

dfs_loop()

explored = dict()
list_d = list(finished_time.items())
list_d.sort(key=lambda d: d[1])
f = dict()
for h in list_d:
    f[h[0]] = h[1]
scc_num = 0
scc_max_sizes = []

for i in f:
    if i not in explored:
        scc_num += 1
        scc_size = 0
        s = i
        dfs(i, 1)

        scc_max_sizes.append(scc_size)

scc_max_sizes.sort(reverse=True)
print(f'SCC max sizes {scc_max_sizes}')
