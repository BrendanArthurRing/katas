a = [1, 4, 10, 6, 2]

def avoidObstacles(arr):
    limit = max(arr) + 2
    remainders = []

    for numerator in range(1, limit):
        for denominator in arr:
            if denominator != 1:
                remainders.append(denominator % numerator)

        print(remainders)

        if 0 not in remainders:
            return numerator

        remainders = []
