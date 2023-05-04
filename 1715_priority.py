from queue import PriorityQueue
N = int(input())
pq = PriorityQueue() #pq라는 변수에 ProrityQueue를 적용하는 것

for _ in range(N):
    pq.put(int(input())) #pq에 숫자를 넣기
    
data1 = 0 ; data2 = 0; sum = 0
while pq.qsize() > 1: #나는 N > 1: 로 했는데 당연히 말이 안됨. 
    data1 = pq.get()
    data2 = pq.get()
    tmp= data1 + data2
    sum += tmp
    pq.put(tmp)

print(sum)