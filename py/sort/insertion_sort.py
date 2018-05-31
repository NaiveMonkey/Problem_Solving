import unittest


def insertion_sort(list):
    for i in range(2, len(list)):
        index = i
        while index > 0 and list[index - 1] > list[index]:
            list[index - 1], list[index] = list[index], list[index - 1]
            index -=1
    return list

class UnitTest(unittest.TestCase):

    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([1, 3, 4, 2, 5, 6]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([1, 4, 2, 3, 6, 5]))

if __name__ == '__main__':
        unittest.main()
