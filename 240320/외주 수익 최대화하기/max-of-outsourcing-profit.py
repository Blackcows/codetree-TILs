n = int(input())

jobs = [list(map(int, input().split())) for _ in range (n)]

time = [job[0] for job in jobs] # 소요 시간
benefit = [job[1] for job in jobs] # 보상

dp = benefit[:]

for i in range(n):
    if time[i] + i > n:
        dp[i] = 0
    for j in range(i):
        if time[j] <= i - j:
            if time[i] + i <= n:
                dp[i] = max(dp[i], dp[j] + benefit[i])

# print(dp)
print(max(dp))

# ========= 이전 풀이 하던거 ==========
# index = -1
# for job in jobs:
#     index += 1 # index 이동
#     if index + job[0] > n:
#         # dp[index] = dp[index-1]
#         break # 날짜 넘어가면 break 처리

#     time = [False for _ in range (n)]

#     # == 이전 job과 충돌 여부 검증 ==
#     for i in range (index, index + job[0]):
#         # 현재 index를 true로
#         time[i] = True

#     # merge가 되거나 처음에 도달하면 stop
#     mergeIndex = -1

#     isConflict = False
#     for j in range (index-1, -1, -1):
#         for k in range (j, j + jobs[j][0]):
#             if time[k] == True:
#                 isConflict = True
#                 break
#             else:
#                 isConflict = False

#         if isConflict != True:
#             mergeIndex = j
#             break
#     # print("merge:", mergeIndex)

#     for i in range (index, index + job[0]):
#         if isConflict == False:
#             dp[i] = max(dp[i-1], dp[i], job[1], dp[mergeIndex] + job[1])
#         else:
#             dp[i] = max(dp[i-1], dp[i], job[1])
#     print(dp)