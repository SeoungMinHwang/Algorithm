# # dfs 구현

# graph = {'A' : ['B','E','G'],
#         'B' : ['A', 'C', 'D'],
#         'C' : ['B'],
#         'D' : ['B'],
#         'E' : ['A', 'F'],
#         'F' : ['E'],
#         'G' : ['A','H','I','J'],
#         'H' : ['G'],
#         'I' : ['G', 'K'],
#         'J' : ['G'],
#         'K' : ['I']}

# visited = []


# def dfs(start):
#     print(start , '->' ,end = ' ')
#     visited.append(start)
    
#     for v in graph[start]:
#         if v not in visited:
#             dfs(v)
            
# dfs('A')

# print()
# #스택 구현

# graph = {'A' : ['B','E','G'],
#         'B' : ['A', 'C', 'D'],
#         'C' : ['B'],
#         'D' : ['B'],
#         'E' : ['A', 'F'],
#         'F' : ['E'],
#         'G' : ['A','H','I','J'],
#         'H' : ['G'],
#         'I' : ['G', 'K'],
#         'J' : ['G'],
#         'K' : ['I']}

# stack = []
# visited = []


# stack.append('A')
# visited.append('A')
# while stack:
#     tmp = stack.pop()
#     print(tmp, '->', end = ' ')
    
#     for i in reversed(graph[tmp]):
#         if i not in visited:
#             stack.append(i)
#             visited.append(i)

# print()


# # BFS 구현

# from collections import deque

# graph = {'A' : ['B','E','G'],
#         'B' : ['A', 'C', 'D'],
#         'C' : ['B'],
#         'D' : ['B'],
#         'E' : ['A', 'F'],
#         'F' : ['E'],
#         'G' : ['A','H','I','J'],
#         'H' : ['G'],
#         'I' : ['G', 'K'],
#         'J' : ['G'],
#         'K' : ['I']}

# Q = deque()
# visited = []


# Q.append('A')
# visited.append('A')
# while Q:
#     tmp = Q.popleft()
#     print(tmp, '->', end = ' ')
    
#     for i in reversed(graph[tmp]):
#         if i not in visited:
#             Q.append(i)
#             visited.append(i)





# n, m = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(n)]


# dp_arr = [[0] * (n+1) for _ in range(n+1)]


# for i in range(1, len(dp_arr)):
#     for j in range(1, len(dp_arr)):
#         dp_arr[i][j] = arr[i-1][j-1] + dp_arr[i-1][j] + dp_arr[i][j-1] - dp_arr[i-1][j-1]



# for i in range(m):
#     x1,y1,x2,y2 = map(int, input().split())
#     print(dp_arr[x2][y2] + dp_arr[x1-1][y1-1] - dp_arr[x2][y1-1] - dp_arr[x1-1][y2])

