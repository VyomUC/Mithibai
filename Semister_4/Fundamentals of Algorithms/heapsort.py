import heapq

def min_heap_sort(arr):
    # Create a min heap from the array
    heapq.heapify(arr)
    result = []
    while arr:
        # Pop the smallest element from the heap
        result.append(heapq.heappop(arr))
    return result

def max_heap_sort(arr):
    # Convert arr to a max heap by negating its elements
    arr = [-x for x in arr]
    heapq.heapify(arr)
    result = []
    while arr:
        # Pop and negate the largest element (stored as smallest in min heap)
        result.append(-heapq.heappop(arr))
    return result

# Example usage
arr = [81, 89, 9, 11, 14, 76, 54, 22]
print(f"Original: {arr}")
print(f"Sorted with Min Heap: {min_heap_sort(arr.copy())}") # Use arr.copy() to not modify the original array
print(f"Sorted with Max Heap: {max_heap_sort(arr.copy())}")