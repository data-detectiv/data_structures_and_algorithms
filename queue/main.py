data = []
data.append(5)
data.append(10)
data.pop(0)
element = data.pop(0)
# print(element)

# from collections import deque allows you to do queue operations in constant time
# basic operations of queue
"""
- Enqueue - add an element to the end of the queue
- Dequeue - remove an element from the front of the queue
- isEmpty - check if the queue is empty
- isFull - check if the queue is full
- peek - get the value from the front of the queue without removing it
"""
class Queue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        if (self.tail == self.k - 1):
            print("The queue is full\n")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail += 1
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print("The queue is empty\n")
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head += 1
            return temp
    
    def printQueue(self):
        if self.head == -1:
            print("No element in the queue")
        else:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
            
queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print("Initial queue")
queue.printQueue()

queue.dequeue()
print("After removing an element from the queue")
queue.printQueue()
