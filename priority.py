#우선순위 큐
from queue import PriorityQueue
myque = PriorityQueue()
myque.put(1)
myque.put(5)
myque.put(3)
myque.put(2)
myque.put(9)
myque.put(4)

#데이터 꺼내기
myque.get()
#1, 2, 3, 4, 5, 9 => 꺼내면 바로 없어짐.

#현재 큐에 들어있는 데이터 건수
myque.qsize()




