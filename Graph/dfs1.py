def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end = " ")
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
graph = {
    "A" : ["B","D", "C"],
    "B" : ["A", "E"],
    "C" : ["A", "F"],
    "D" : ["A","F"],
    "E" : ["B","G"],
    "F" : ["C","D", "H"],
    "G" : ["E","H", 'I'],
    "H" : ["F","G","J"],
    "I" : ["G", "J"],
    "J" : ["H","I"]
}

visited = set()
dfs(graph, "A", visited) 