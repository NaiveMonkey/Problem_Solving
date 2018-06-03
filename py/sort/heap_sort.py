def heap_sort(list):

    def swap(list, index, largest):
        list[index], list[largest] = list[largest], list[index]

    def sift_down(list, index, size):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left <= size - 1 and list[left] > list[index]:
            largest = left

        if right <= size - 1 and list[right] > list[largest]:
            largest = right

        if largest != index:
            swap(list, index, largest)
            sift_down(list, largest, size)

    def heapify(list, size):
        index = (size // 2) - 1
        while index >= 0:
            sift_down(list, index, size)
            index -= 1

    size = len(list)
    heapify(list, size)
    end = size - 1
    while end > 0:
        swap(list, 0, end)
        sift_down(list, 0, end)
        end -= 1


list = [1, 3, 2, 4, 9, 7]
heap_sort(list)
print(list)
