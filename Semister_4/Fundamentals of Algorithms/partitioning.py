def partitioning(l, k):
    if not l or k <= 0:
        return []

    # Choose the first element as the pivot
    pivot = l[0]
    left = [n for n in l if n < pivot]
    middle = [n for n in l if n == pivot]
    right = [n for n in l if n > pivot]

    if k <= len(left):
        # If k is within the range of the left partition, recurse only into the left.
        return partitioning(left, k)
    elif k <= len(left) + len(middle):
        # If k falls within the left and middle partitions, return those parts.
        return left + middle[:k - len(left)]
    else:
        # If k extends into the right partition, include the appropriate portion of the right.
        return left + middle + partitioning(right, k - len(left) - len(middle))

k = 3
l = [4, 6, 1, 0, 10, -3, 0, 0, 0, -3]
output = partitioning(l, k)
print(f"Output: {output}")

# For comparison, showing the expected first k smallest elements by direct sorting
l.sort()
expected = l[:k]
print(f"Expected: {expected}")