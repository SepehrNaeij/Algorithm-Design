
def find_combinations(arr, target):
    arr.sort()
    if target == 0:
        return [[]]
    result = []

    # loop through the array to find all possible combinations that add up to the target
    for i in range(len(arr)):
        # if the current number is greater than the target, break out of the loop
        if arr[i] > target:
            break
        # recursively call the function with a new target and the remaining elements of the array
        new_target = target - arr[i]
        remaining_arr = arr[i:]
        sub_result = find_combinations(remaining_arr, new_target)
        # append the current number to each combination found by the recursive call
        for combo in sub_result:
            combo.append(arr[i])
            result.append(combo)
    return result

arr = list(map(int, input().split(' ')))
target = int(input())
combinations = find_combinations(arr, target)
for combo in combinations:
    print(combo)