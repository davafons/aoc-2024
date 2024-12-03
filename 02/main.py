def input_generator():
    with open("input.txt", "r") as file:
        for line in file:
            yield list(map(int, line.strip().split()))


def calculate_unsafe_points(data_points, i):
    failed_points = 0

    first_iteration = True
    increasing = True

    while i < len(data_points):
        j = i + 1
        while j < len(data_points):
            if first_iteration:
                increasing = data_points[j] > data_points[i]

            diff = abs(data_points[i] - data_points[j])
            print(f"Pair [{i}]={data_points[i]}, [{j}]={data_points[j]}, diff={diff}")
            if diff > 3 or diff == 0:
                print("ERROR: Invalid diff")
                failed_points += 1
            elif data_points[i] < data_points[j] and not increasing:
                print("ERROR: Started to increase")
                failed_points += 1
            elif data_points[i] > data_points[j] and increasing:
                print("ERROR: Started to decrease")
                failed_points += 1
            else:
                print("Safe")
                break

            j += 1

        first_iteration = False
        i = j

    return failed_points


def safe_levels(input_generator, tolerance):
    safe_levels = 0
    for data_points in input_generator():
        print("----------------")
        print(data_points)
        for i in range(0, tolerance + 1):
            print(f"> start: {i}, tolerance: {tolerance - i}")
            if calculate_unsafe_points(data_points, i) <= tolerance - i:
                safe_levels += 1
                print("Level is safe")
                break

    print(f"Safe levels: {safe_levels}")

    return safe_levels


# print(f"Part one: {safe_levels(input_generator, tolerance=0)}")
print(f"Part two: {safe_levels(input_generator, tolerance=1)}")
