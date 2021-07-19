import unittest

from tarea_22 import max_milk


class tarea_22_tests(unittest.TestCase):
    def test_1(self):
        """Test 1"""
        number_of_cows = 4
        max_weight = 10
        weight_of_cows = [1,2,3,4]
        milk_of_cows = [4,3,2,1]
        self.assertEqual(10, max_milk(number_of_cows,max_weight,weight_of_cows,milk_of_cows))
    def test_2(self):
        """Test 2"""
        number_of_cows = 3
        max_weight = 10
        weight_of_cows = [7,5,5]
        milk_of_cows = [8,5,5]
        self.assertEqual(10, max_milk(number_of_cows,max_weight,weight_of_cows,milk_of_cows))
    def test_3(self):
        """Test 2"""
        number_of_cows = 10
        max_weight = 2000
        weight_of_cows = [200,250,100,200,250,450,300,300,175,350]
        milk_of_cows = [8,5,5,4,6,6,7,8,10,9]
        self.assertEqual(58, max_milk(number_of_cows,max_weight,weight_of_cows,milk_of_cows))
        
        



if __name__ == '__main__':
    unittest.main()