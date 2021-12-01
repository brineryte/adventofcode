# * Part One
with open('../inputs/input1.txt') as f:
    measurements = f.read().splitlines()
    prev = 0
    count = -1  # ignore first comparison
    for measurement in measurements:
        count += 1 if int(measurement) > prev else 0
        prev = int(measurement)

    print(increased := count)

# * Part Two
with open('../inputs/input1.txt') as f:
    measurements_str = f.read().splitlines()
    measurements = [int(x) for x in measurements_str]
    window_size = 3
    increases = 0

    for i, m in enumerate(measurements[:-window_size]):
        window_1 = measurements[i:i+window_size]
        window_2 = measurements[i+1:i+1+window_size]

        increases += 1 if sum(window_2) > sum(window_1) else 0

    print(walrus := increases)
