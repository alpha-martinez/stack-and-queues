from collections import deque

rome_queue = deque()
rome_queue.append(1)
rome_queue.append(5)
rome_queue.append(10)

print(rome_queue)

rome_queue.popleft()

print(rome_queue)
