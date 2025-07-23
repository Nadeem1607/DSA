def sumFinder(arr, target):
    s=set()
    for num in arr:
        remain = target - num
        if remain in s:
            return True
        s.add(num)
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2
    print(sumFinder(arr, target))
    