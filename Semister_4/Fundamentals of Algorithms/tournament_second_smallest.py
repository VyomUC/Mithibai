def tournament_for_second_smallest(arr):
    if len(arr) < 2:
        return "Array does not have enough elements."

    # Initialize the tournament structure.
    opps = {x: [] for x in arr}
    
    # Perform the tournament.
    while len(arr) > 1:
        new_arr = []
        for i in range(0, len(arr), 2):
            if i+1 < len(arr):
                if arr[i] < arr[i+1]:
                    opps[arr[i]].append(arr[i+1])
                    new_arr.append(arr[i])
                else:
                    opps[arr[i+1]].append(arr[i])
                    new_arr.append(arr[i+1])
            else:
                # For the last element in case of odd number of elements
                new_arr.append(arr[i])
        arr = new_arr

    # The winner of the tournament is the smallest element.
    winner = arr[0]
    
    # Find the second smallest by finding the minimum in the opponents of the winner.
    second_smallest = min(opps[winner]) if opps[winner] else "Array does not have enough elements."
    return second_smallest

arr = [5, 10, 2, 19, 13, 11, 18, 6, 4, 17]
print(f"Original array: {arr}")
print(f"2nd smallest element: {tournament_for_second_smallest(arr)}")