
N , K = map(int, input().split())
A = [0] * N #A라는 리스트에 빈 깡통 만들기

for i in range(N):
    A[i] = int(input()) #A라는 빈 깡통에 숫자 넣기
    
cnt = 0
for x in range(N-1,-1,-1): #큰 값에서 역순으로 for문 돌리기
    if A[x] <= K:
        cnt += int(K / A[x])
        K = K % A[x]
    
print(cnt)

