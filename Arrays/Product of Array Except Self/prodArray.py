def prodArray(arr):
    z=0
    prod=1
    ind = []
    for i in range(len(arr)):
        if arr[i] == 0:
            z += 1
            ind.append(i)
        else:
            prod *= arr[i]
    if z > 1:
        return [0] * len(arr)
    elif z == 1:
        result = [0] * len(arr)
        result[ind[0]] = prod
        return result
    else:
        return [prod // arr[i] for i in range(len(arr))]
    return []

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(prodArray(arr))