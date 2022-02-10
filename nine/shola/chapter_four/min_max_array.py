arr = [1, 2, 3, 4, 5]

minimum_sum = 0
maximum_sum = 0
minimum = min(arr)
maximum = max(arr)

for i in range(len(arr)):
    if arr[i] != minimum:
        maximum_sum += arr[i]
    if arr[i] != maximum:
        minimum_sum += arr[i]

print(minimum_sum, maximum_sum)
