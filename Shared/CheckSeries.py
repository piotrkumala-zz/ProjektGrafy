def CheckSeries(a: [], n: int):
    a.sort(reverse=True)
    while True:
        empty = True
        negative = False
        for x in a:
            if x != 0:
                empty = False
            if x < 0:
                negative = True
        if empty:
            return True
        elif a[0] < 0 or a[0] >= n or negative:
            return False
        else:
            i = 1
            while i <= a[0]:
                a[i] -= 1
                i += 1
            a[0] = 0
            a.sort(reverse=True)
