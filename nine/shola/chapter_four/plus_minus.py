arr = [1, 1, 0, -1, -1]
positive_count = 0
negative_count = 0
zero_count = 0

for i in range(len(arr)):
    if arr[i] > 0:
        positive_count += 1
    elif arr[i] < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f'{positive_count/len(arr):.6f}')
print(f'{negative_count/len(arr):.6f}')
print(f'{zero_count/len(arr):.6f}')

