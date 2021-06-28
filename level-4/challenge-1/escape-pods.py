# This is a flow network problem that utilizes Dinic's Algorithm to compute the maximum flow in the network
# An alternate approach can use the Ford-Fulkerson Method but it will take more time to run
def solution(entrances, exits, path):
    max_val = sum(list(map(sum, path)))
    level_graph = []
    # Construct level graph
    for i in range(len(path)):
        level_graph.append([])
        for j in range(len(path[i])):
            level_graph[i].append([0, path[i][j]])
        level_graph[i].append([0, 0])
        if i in exits:
            level_graph[i].append([0, max_val])
        else:
            level_graph[i].append([0, 0])
    level_graph.append([])
    level_graph.append([])
    for i in range(len(path[0]) + 2):
        if i in entrances:
            level_graph[-2].append([0, max_val])
        else:
            level_graph[-2].append([0, 0])
        level_graph[-1].append([0, 0])
    # Use BFS to determine if there exists an augmenting path in level graph
    while bfs(level_graph, len(level_graph) - 2, len(level_graph) - 1):
        pass
    # Calculate the max flow
    max_flow = 0
    for i in range(len(level_graph)):
        max_flow += level_graph[-2][i][0]
    return max_flow

# Breadth first shortest path function
def bfs(matrix, source, destination):
    visited = [-1 for i in range(len(matrix))]
    visited[source] = source
    queue = [source]
    while len(queue) > 0:
        tail = queue.pop(0)
        for i in range(len(matrix)):
            if ((matrix[tail][i][1] - matrix[tail][i][0]) != 0) and (visited[i] == -1):
                if i == destination:
                    # Get the route
                    visited[destination] = tail
                    path = [destination]
                    tmp = destination
                    while tmp != source:
                        tmp = visited[tmp]
                        path.append(tmp)
                    path.reverse()
                    tmp = 1
                    # Unbounded upper value
                    residual_capacity = float('inf')
                    current = source
                    # Get flow value and update augmented path
                    while tmp != len(path):
                        entry = matrix[current][path[tmp]]
                        diff = abs(entry[1]) - entry[0]
                        residual_capacity = min(residual_capacity, diff)
                        current = path[tmp]
                        tmp += 1
                    tmp = 1
                    current = source
                    while tmp != len(path):
                        entry = matrix[current][path[tmp]]
                        if entry[1] < 0:
                            entry[1] += residual_capacity
                        else:
                            entry[0] += residual_capacity
                        entry = matrix[path[tmp]][current]
                        if entry[1] <= 0:
                            entry[1] -= residual_capacity
                        else:
                            entry[0] += residual_capacity
                        current = path[tmp]
                        tmp += 1
                    # The sink can be reached
                    return True
                else:
                    visited[i] = tail
                    queue.append(i)
    # This sink cannot be reached
    return False

# Test function
def main():
    print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))

# Run test
main()