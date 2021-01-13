from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)
# deque([0, 1, 2, 3, 4])


deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)  # deque([0, 1, 2, 3, 4])
deque_list.appendleft(10)
print(deque_list)  # deque([10, 0, 1, 2, 3, 4])


deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)  # deque([0, 1, 2, 3, 4])
deque_list.rotate(2)
print(deque_list)  # deque([3, 4, 0, 1, 2])
deque_list.rotate(2)
print(deque_list)  # deque([1, 2, 3, 4, 0])


deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)  # deque([0, 1, 2, 3, 4])
print(deque(reversed(deque_list)))  # deque([4, 3, 2, 1, 0])


deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)  # deque([0, 1, 2, 3, 4])
deque_list.extend([5, 6, 7])
print(deque_list)  # deque([0, 1, 2, 3, 4, 5, 6, 7])


deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)  # deque([0, 1, 2, 3, 4])
deque_list.extendleft([5, 6, 7])
print(deque_list)  # deque([7, 6, 5, 0, 1, 2, 3, 4])
