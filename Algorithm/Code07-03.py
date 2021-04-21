def isQueueFull():
    global SIZE, queue, front, rear
    if(rear == SIZE -1):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if(front == rear):
        return True
    else:
        return False

SIZE = 5
queue = ['화사', '솔라', '분별', '휘인', '선미']
front = -1
rear = 4

print("큐 꽉?", isQueueFull())

queue = [None, None, None, None, None]
front = 2
rear = 2
print('큐 텅?', isQueueEmpty())