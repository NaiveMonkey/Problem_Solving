import unittest


def bubble_sort(list):

    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


class UnitTest(unittest.TestCase):

    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], bubble_sort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubble_sort([1, 3, 4, 2, 5, 6]))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubble_sort([1, 4, 2, 3, 6, 5]))

if __name__ == '__main__':
    unittest.main()