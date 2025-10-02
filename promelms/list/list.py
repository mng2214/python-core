# find common elements in arr
def find_common_elements (a1: list, a2: list) -> list:
    result = []
    for i in a1:
        if i in a2:
            result.append(i)
    return result

# find unique elements in arr
def find_diff_elements (a1: list, a2: list) -> list:
    result = []
    for i in a1:
        if i not in a2:
            result.append(i)
    return result


if __name__ == '__main__':

    arr1 = [1,2,3,4,5]
    arr2 = [1,2,6,6,5]

    result_arr_common = find_common_elements(arr1, arr2)
    result_arr_diff = find_diff_elements(arr1, arr2)

    print(result_arr_common)
    print(result_arr_diff)