#https://www.acmicpc.net/problem/13305

import sys

input = sys.stdin.readline

n = int(input())

distance = list(map(int, input().split()))
cities = list(map(int, input().split()))


dis = 0
solve = 0
for i in range(n-2,0,-1):
    dis += distance[i]
    if cities[i] <= cities[i-1]:
        solve += cities[i] * dis
        dis = 0
    else:
        pass
solve += distance[0] * cities[0]

print(solve)



##### 개선된 풀이 #############
import sys
input = sys.stdin.readline

N = int(input())

roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

# 첫번째 값 더하기
min_price = roads[0] * costs[0]

# 가장 값이 싼 주유소 지정
min_cost = costs[0]

for i in range(1, N-1):
  if min_cost > costs[i]: # 가장 값이 싼 주유소가 현재 주유소 보다 비싸면 바꿔준다.
    min_cost = costs[i] # 값 싼 주유소로 바꿔주기
  
  min_price += min_cost * roads[i]

print(min_price)