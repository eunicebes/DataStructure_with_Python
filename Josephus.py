import sys
import circular_queue

Q = circular_queue.CircularQueue()
n = int(input("Enter an integer (1-100): "))

for i in range(1, n+1, 1):
    Q.enqueue(i)

for i in range(n):
    temp = Q.dequeue()
    Q.dequeue()
    Q.enqueue(temp)

print("The value of J({0}) is: {1}".format(n, Q.queue[Q.head]))