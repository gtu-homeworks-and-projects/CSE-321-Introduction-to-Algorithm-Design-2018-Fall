from xlrd import open_workbook

def dfs(graph, start):
    visited = []
    stack = [start]
    while len(stack) > 0:
        vertex = stack.pop() # pops last element from the list. Just as a stack
        if vertex not in visited:
            visited.append(vertex)
            if (vertex < len(graph)):
                stack.extend(graph[vertex]) 
    return visited

def bfs(graph, start):
    visited = []
    queue = [start]
    while len(queue):
        vertex = queue.pop(0) # pops first element from the list just as queue
        if vertex not in visited:
            visited.append(vertex)
            if (vertex < len(graph)):
                queue.extend(graph[vertex]) 
    return visited

# Graph from excell file
wb = open_workbook("Graph_data.XLS")
s = wb.sheets()[0]
values = {}
for row in range(3,20):
    single_row = []
    for col in range(2):
        value = (s.cell(row,col).value)
        value = int(value)
        single_row.append(value)
    if (len(values) < single_row[0]):
        values[single_row[0]] = [single_row[1]]
    else:
        values[single_row[0]].append(single_row[1])
graph = values
#

print("Vertices of graph:", end=' ')
for adjacents in graph:
    print(adjacents, end=' ')

print("")

for adjacents in graph:
    print("Adjacents of ", adjacents, ":" , graph[adjacents])

startVertex = 1
print("Depth First Search")
print(dfs(graph,1))

print("Breadth First Search")
print(bfs(graph, 1))