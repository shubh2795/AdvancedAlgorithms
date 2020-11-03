import unittest
import KnapsackProblem


class TestKnapsackMethods(unittest.TestCase):

    def knapsack_recursive_uts(self):
        n1 = 20
        n2 = 30
        n3 = 25
        n4 = 29
        m = len(KnapsackProblem.weight)
        print('\n***** Knapsack recursive test 01 ************')

        o1 = KnapsackProblem.knapsack_recursive(m, n1)
        o2 = KnapsackProblem.knapsack_recursive(m, n2)
        o3 = KnapsackProblem.knapsack_recursive(m, n3)
        o4=KnapsackProblem.knapsack_recursive(m, n4)
        self.assertFalse(o1)
        self.assertTrue(o2)
        self.assertFalse(o3)
        self.assertTrue(o4)
        print('Assign 01: UT 01: passed...')


if __name__ == '__main__':
    unittest.main()
