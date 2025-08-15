n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 1
dst = 2
k = 1
adj = {}
def add_edge(x, y, w):
    if x not in adj:
        adj[x] = []
    if y not in adj:
        adj[y] = []
    adj[x].append([y,w])

for u, v, w in flights:
    add_edge(u, v, w)

visited = [0] * 1000000
new_price = float("inf")
def dfs(src, dst, k, price):
    global new_price
    if src == dst and k >= 0:
        new_price = min(new_price, price)
        return 
    if k < 0:
        return -1
    for neighbor, weight in adj[src]:
        if weight + price < new_price:
            dfs(neighbor, dst, k-1, weight + price)

dfs(src,dst,k,0)

if new_price == float("inf"):
    print(-1)
else:
    print(new_price)