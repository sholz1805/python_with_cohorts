a = [1, 2, 3]
b = [3, 2, 1]

a_counter = 0
b_counter = 0

for i in range(len(a)):
    if a[i] > b[i]:
        a_counter += 1
    elif a[i] < b[i]:
        b_counter += 1
    else:
        pass
print(a_counter, b_counter)



