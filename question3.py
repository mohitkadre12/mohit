def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=' ')

    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example data
if __name__ == "__main__":
    # This is the graph, represented as an adjacency list (dictionary of lists)
    graph = {
        0: [1, 2],  # Node 0 is connected to nodes 1 and 2
        1: [0, 3, 4],  # Node 1 is connected to nodes 0, 3, and 4
        2: [0, 5],  # Node 2 is connected to nodes 0 and 5
        3: [1],  # Node 3 is connected to node 1
        4: [1],  # Node 4 is connected to node 1
        5: [2]  # Node 5 is connected to node 2
    }

    visited = set()

    # Start DFS from node 0
    print("DFS Traversal starting from vertex 0:")
    dfs(graph, 0, visited)  
