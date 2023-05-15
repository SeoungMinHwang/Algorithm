#https://www.acmicpc.net/problem/1043

#유니온 파인드
def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    if a <= b:
        parent[find(b)] = find(a)
    else:
        parent[find(a)] = find(b)
    
    
people, party = map(int, input().split())
parent = [i for i in range(0,people + 1)]
truth = list(map(int, input().split()))
parties = []
for i in range(party):
    parties.append(list(map(int, input().split())))

if truth == [0]:
    print(party)
    
else:
    for i in truth[1:]:
        union(truth[0],i)


    for p in parties:
        if p[0] == 1:
            pass
        else:
            for j in p[2:]:
                union(p[1], j)
                
    count = 0    
    for p in parties:
        if find(truth[1]) != find(p[1]):
            count += 1

    print(count)