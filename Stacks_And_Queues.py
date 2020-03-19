stack = [0] * N
size = 0


def push(x):
    global size
    stack[size] = x
    size += 1


def pop():
    global size
    size -= 1
    return stack[size]


queue = [0] * N
head, tail = 0, 0


def push(x):
    global tail
    tail = (tail + 1) % N
    queue[tail] = x


def pop():
    global head
    head = (head + 1) % N
    return queue[head]


def size():
    return (tail - head + N) % N


def empty():
    return head == tail


def grocery_store(A):
    n = len(A)
    size, result = 0, 0
    for i in range(n):
        if A[i] == 0:
            size += 1
        else:
            size -= 1
            result = max(result, -size)
    return result

