from collections import deque

class QueueStack:
  def __init__(self):
    self.queue = deque()
    print(self.queue)

  def push(self, val):
    self.queue.append(val)

  def pop(self):
    return self.queue.pop()

  def peek(self):
    return list(self.queue)[-1]

  def empty(self):
    return len(list(self.queue)) == 0

q = QueueStack()
print(q.empty())
q.push(4)
print(q.empty())
q.push(5)
q.push(6)
q.push(7)
print(q.peek())
print(q.pop())
print(q.pop())