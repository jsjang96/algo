#plus
#minus
#one
#zero
from queue import PriorityQueue
N = int(input())

plus_pq = PriorityQueue()
minus_pq = PriorityQueue()
one = 0
zero = 0
sum = 0
for i in range(N):
    data = int(input())
    if data > 1:
        plus_pq.put(data * -1)
    elif data ==1:
        one +=1
    elif data ==0:
        zero+=1
    else:
        minus_pq.put(data)
        
while plus_pq.qsize() > 1:
    first = plus_pq.get() * -1
    second = plus_pq.get() * -1
    sum += first * second

if plus_pq.qsize() > 0:
    sum += plus_pq.get() * -1
    
while minus_pq.qsize() > 1:
    first = minus_pq.get()
    second = minus_pq.get()
    sum += first * second
    
if minus_pq.qsize() >0:
    if zero == 0:
        sum += minus_pq.get()
    
sum += one
print(sum)
    
    
    
