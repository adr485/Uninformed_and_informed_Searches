def find(d,m):
    keys = [k for k, v in d.items() if v==m]
    return keys[0]

n=int(input("Eneter num of nodes-"))
graph={}
hd={}
for i in range(n):
    node=int(input("Enter the node-"))
    adj=map(int,input("Enter the adjacent nodes of it-").split())
    graph[node]=adj
for i in range(n):
    vertex=int(input('enter vertex: '))
    dist=int(input('enter heuristic distance: '))
    hd[vertex]=dist

src=int(input("Enter the source node-"))
Goal=int(input("Eneter the goal node- "))
visited = []
queue = []    

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        sk = queue.pop(0)      
        print (sk, end = " ")
        if sk==Goal:
            break
        m=99999
        for i in graph[sk]:
             if i not in visited:
                visited.append(i)
                if m>hd[i]:
                    m=hd[i]
        queue.append(find(hd,m))
bfs(visited, graph, src)