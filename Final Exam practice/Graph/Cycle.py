#Kiem tra chu trinh
def reset_visited(visited):
    visited = [0] * (n + 1)
def reset_par(parent):
    parent = [-1] * (n + 1)

def check_cycle_by_dfs(u, par, visited):
    visited[u] = 1
    for v in adj[u]:
        if not visited[v]:
            if check_cycle_by_dfs(v, u, visited):
                return True
        elif v != par:
            start = v, end = u
            return True
    return False
if __name__ == "__main__":
    n, m = map(int, input().split())
    adj = {}
    visited = [0] * (n + 1)
    parent = [-1] * (n + 1)
    global start, end
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)

    # Dung dfs de check chu trinh vo huong (do thi lien thong)
    if check_cycle_by_dfs(0, -1, visited):
        print("Do thi co chu trinh")
    else:
        print("Do thi khong co chu trinh")
    # Dung dfs de check chu trinh vo huong (do thi lien thong)
    cnt = 1
    for u in range(n):
        if not visited[u]:
            if check_cycle_by_dfs(u, -1, visited):
                print(f"Do thi lien thong thu {cnt} co chu trinh")
            else:
                print(f"Do thi lien thong thu {cnt} khong co chu trinh")
            cnt += 1
            

        
