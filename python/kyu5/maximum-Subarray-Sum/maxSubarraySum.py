def max_sequence(arr):
    x = 0
    y = 2
    a = []
    d = 2
    positive = []
    for b in arr:
        if b <= 0:
            positive.append(False)
        else:
            positive.append(True)
    if len(arr) == 0:
        somatotal = 0
    elif all(positive) and any(positive):
        somatotal = sum(arr)
    elif max(arr) <= 0:
        somatotal = 0
    else:
        while d <= len(arr):
            while y <= len(arr):
                a.append(sum(arr[x:y]))
                x = x + 1
                y = y + 1
            x = 0
            y = d + 1
            d = d + 1
        somatotal = max(a)
    return somatotal
