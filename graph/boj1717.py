#https://www.acmicpc.net/problem/1717
# 유니온 파인드
import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a,b = map(int, input().split())
parent_list = list(range(a+1))

def find(a):
    if parent_list[a] == a:
        return a
    else:
        #이 부분이 핵심 find를 수행하며 루트 노드에 성형으로 1path만에 갈 수 있도록 연결해줌 
        #경로 압축!
        parent_list[a] = find(parent_list[a])
        return parent_list[a]

def union(a,b):
    parent_list[find(b)] = find(a)
    
def check(a,b):
    if find(a)==find(b):return True
    else: return False
    
    
for i in range(b):
    a,b,c = map(int,input().split())
    if a == 0:
        union(b,c)
    else:
        if check(b,c):print("YES")
        else:print("NO")