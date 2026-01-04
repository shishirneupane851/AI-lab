city = {         #city routes by dfs
 "Home": ["A","B"],
 "A": ["C"],
 "B": ["C"],
 "C": []
}

path = []

def dfs(x):
    path.append(x)
    if x == "C":
        print(path)
    for y in city[x]:
        dfs(y)
    path.pop()

dfs("Home")
