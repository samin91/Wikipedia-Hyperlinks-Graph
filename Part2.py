from collections import deque


def bfs(graph, start, goal):
    if start == goal:
        print([start])
        return

    queue = deque([start])

    # dict which holds parents, later helpful to retreive path.
    # Also useful to keep track of visited node
    parent = {}
    parent[start] = start

    while queue:
        currNode = queue.popleft()
        for neighbor in graph[currNode]:
            # goal found
            if neighbor == goal:
                parent[neighbor] = currNode
                print_path(parent, neighbor, start)
                return
            # check if neighbor already seen
            if neighbor not in parent:
                parent[neighbor] = currNode
                queue.append(neighbor)
    print("No path found.")


def print_path(parent, goal, start):
    path = [goal]
    # trace the path back till we reach start
    while goal != start:
        goal = parent[goal]
        path.insert(0, goal)
    print(path)


if __name__ == '__main__':
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])
             ` }

    bfs(graph, 'D', 'F')

