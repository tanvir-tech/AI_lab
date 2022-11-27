graph={'a':['b','c','d'],'b':['e'],'c':['d','e'],'d':[],'e':[]}
visited=set()
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbor in graph[root]:
            dfs(visited,graph,neighbor)

dfs(visited,graph,'a')
