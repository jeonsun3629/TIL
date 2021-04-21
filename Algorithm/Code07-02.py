queue = ['화사', '솔라', '문별', None, None]
front = -1
rear = 2

print("==== 큐 상태 ====")
print('[출구] <--', end = '')
for i in range(len(queue)) :
    print(queue[i], end = ' ')
print('<-- 입구')

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)
front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)
front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)
print('----------')

print("==== 큐 상태 ====")
print('[출구] <--', end = '')
for i in range(len(queue)) :
    print(queue[i], end = ' ')
print('<-- 입구')