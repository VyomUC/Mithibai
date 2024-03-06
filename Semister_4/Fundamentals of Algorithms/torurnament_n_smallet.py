import random

def tournament_for_nth_smallest(arr, n):
    if n > len(arr) or n < 1:
        return "Invalid value of n"

    # Structure to hold the matches and results
    matches = []

    # First round: all elements
    matches.append(arr.copy())

    # Conduct the tournament until we find the smallest element
    while len(matches[-1]) > 1:
        next_round = []
        round_matches = matches[-1]
        for i in range(0, len(round_matches), 2):
            if i + 1 < len(round_matches):
                if round_matches[i] < round_matches[i + 1]:
                    next_round.append(round_matches[i])
                else:
                    next_round.append(round_matches[i + 1])
            else:
                # For odd element out
                next_round.append(round_matches[i])
        matches.append(next_round)

    # Smallest element
    smallest = matches[-1][0]
    if n == 1:
        return smallest

    # Find nth smallest by looking back through the tournament matches
    candidates = set()
    for round in matches:
        for i, elem in enumerate(round):
            if elem == smallest:
                # Add the opponents of the smallest element in each round to the candidates
                if i % 2 == 0 and i + 1 < len(round):
                    candidates.add(round[i + 1])
                elif i % 2 != 0:
                    candidates.add(round[i - 1])
    
    # Sort the candidates to find the nth smallest
    sorted_candidates = sorted(list(candidates))

    # n - 1 because we exclude the smallest element found earlier
    if n - 1 <= len(sorted_candidates):
        return sorted_candidates[n - 2]
    else:
        return "n is too large"

arr = [5, 10, 2, 19, 13, 11, 18, 6, 4, 17]
n = int(input("Enter n: "))
print(f"{n}th smallest element: {tournament_for_nth_smallest(arr, n)}")