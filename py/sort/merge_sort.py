import unittest


def merge_sort(list):

    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]

        print('left:' + str(merge_sort(left_half)))
        print('right: ' + str(merge_sort(right_half)))

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1
            # print('a: ' + str(list))

        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1
            # print('b: ' + str(list))

        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1
            # print('c: ' + str(list))

    return list


list = [6, 2, 4, 1, 3, 7, 5, 8]
merge_sort(list)
print(list)
