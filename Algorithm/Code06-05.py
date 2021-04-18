def isStackEmpty():
    global SIZE, stack, top
    if(top == -1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if(isStackFull()):
        print("스택 꽉!")
        return
    top += 1
    stack[top] = data

def pop() :
    global SIZE, stack, top
    if(isStackEmpty()):
        print("스택 텅!")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

# SIZE = 5
# stack = ['커피', '녹차', '꿀물', '콜라', None]
# top = 3

SIZE = 5
stack = ['커피', None, None, None, None]
top = 0

print(stack)
retData = pop()
print('추출 데이터 -->', retData)
print(stack)
retData = pop()
print('추출 데이터 -->', retData)