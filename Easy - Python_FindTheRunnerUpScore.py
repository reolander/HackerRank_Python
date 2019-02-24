if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    first, second = float('-inf'), float('-inf')
    for a in arr:
        if a > first:
            second = first
            first = a
        elif a < first and a > second:
            second = a
    print second
    

