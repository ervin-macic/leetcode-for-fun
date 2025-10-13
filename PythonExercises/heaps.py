def heapify(a, i):
    N = len(a)
    left = 2*i + 1
    right = 2*i + 2
    largest = i

    if left < N and a[left] > a[largest]:
        largest = left
    if right < N and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, largest)


def make_max_heap(a):
    N = len(a)
    for i in reversed(range(N//2)):
        heapify(a, i)


def return_max(a):
    return a[0] if a else None


def increase_key(a, i, new_value):
    a[i] = new_value
    while i > 0 and a[i] > a[(i-1)//2]:
        a[i], a[(i-1)//2] = a[(i-1)//2], a[i]
        i = (i-1)//2
    return i


def extract_max(a):
    if not a:
        return None
    max_val = a[0]
    a[0] = a[-1]
    a.pop()
    if a:
        heapify(a, 0)
    return max_val


def insert(a, x):
    a.append(float("-inf"))       # temporary -inf
    increase_key(a, len(a)-1, x)  # fix position


def delete(a, i):
    if i >= len(a):
        return
    a[i] = a[-1]
    a.pop()
    if i < len(a):
        heapify(a, i)
        increase_key(a, i, a[i])  # ensure upward correctness


def main():
    a = [4, 3, 6, 5, 2, 7, 10]
    make_max_heap(a)
    print("Heap:", a)

    print("Extract max:", extract_max(a))
    print("Heap after extract:", a)

    insert(a, 12)
    print("Heap after insert 12:", a)

    delete(a, 2)
    print("Heap after delete index 2:", a)


main()
