from queue import Queue

q = Queue()

q.put(5)
q.put(6)

print(q.empty())
print(q.qsize())
print(q.get())
print(q.qsize())