def find_nobel_integer(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)):
        if i == arr[i]:
            return 1
    return -1

input_array = list(map(int, input().split()))
print(find_nobel_integer(input_array))
