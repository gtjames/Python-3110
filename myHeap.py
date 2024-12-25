import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

# Test the function
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
res = heapq.heappop(h)
print(res)