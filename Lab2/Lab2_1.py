from Shared.CheckSeries import CheckSeries

series = [7, 7, 5, 5, 3, 3, 1, 1]
print(series)
print(CheckSeries(series, 8))
series = [7, 5, 5, 5, 3, 3, 2, 1, 1, 0]
print(series)
print(CheckSeries(series, 10))
series = [5, 2, 1, 1]
print(series)
print(CheckSeries(series, 4))
