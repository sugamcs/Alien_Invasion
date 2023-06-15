def binary_search(list,target):
    start = 0
    mid = 0
    end = len(list) - 1
    position = -1
    while start <= end:
        mid = (start + end) //2
        if list[mid] == target:
            position = mid
            return f"found {my_target} at position {position + 1}"
        elif list[mid] < target:
            start = mid + 1
        elif list[mid] > target:
            end = mid - 1
    return -1

my_list = [1,2,3,300,34280,43824973,4328748932715]
my_target = 43824973

print(binary_search(my_list,my_target))

