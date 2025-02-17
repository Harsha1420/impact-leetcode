def canPlaceCows(stalls, k, min_dist):
    count = 1
    last_pos = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_pos >= min_dist:
            count += 1
            last_pos = stalls[i]
            if count == k:
                return True

    return False

def aggressiveCows(stalls, k):
    stalls.sort()
    low, high = 1, stalls[-1] - stalls[0]
    best = 0

    while low <= high:
        mid = (low + high) // 2
        if canPlaceCows(stalls, k, mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    return best

stalls1 = [1, 2, 4, 8, 9]
k1 = 3
print(aggressiveCows(stalls1, k1))

stalls2 = [10, 1, 2, 7, 5]
k2 = 3
print(aggressiveCows(stalls2, k2))