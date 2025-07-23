def duplicateFind(arr):
    n = max(arr) + 1
    freq = [0] * n
    result = []
    for num in arr:
        freq[num] += 1
    for i in range(n):
        if freq[i] > 1:
            result.append(i)
    if not result:
        result.append(-1)
    return result

if __name__ == "__main__":
    arr = [1, 2, 3, 6, 3, 6, 1]
    print(duplicateFind(arr))