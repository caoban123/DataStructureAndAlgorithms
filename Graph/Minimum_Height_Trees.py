n = 7
edges = [[1,0],[0,3],[0,5],[0,2],[1,4],[5,6]]
adj = {i: [] for i in range(n)}
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
stack = [node for node in adj if len(adj[node]) == 1]
remain = n
while remain > 2:
    new_stack = []
    for leaf in stack:
        if adj[leaf]:  
            parent = adj[leaf].pop()  
            adj[parent].remove(leaf)  
            if len(adj[parent]) == 1:  
                new_stack.append(parent)
        remain -= 1
    stack = new_stack  
print(stack)