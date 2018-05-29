import unittest


def selection_sort(list):

    for i in range(len(list) - 1):
        min = i
        j = i + 1

        while j < len(list):
            if list[j] < list[min]:
                min = j
            j += 1

        if min is not i:
            list[min], list[i] = list[i], list[min]

    return list

class UnitTest(unittest.TestCase):

    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([1, 3, 4, 2, 5, 6]))
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([1, 4, 2, 3, 6, 5]))

if __name__ == '__main__':
    unittest.main()
