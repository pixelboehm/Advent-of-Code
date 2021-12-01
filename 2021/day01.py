import unittest

class Ship():

    def main(self):
        measurements = []
        with open ("input_day01.txt") as file_measurements: 
            measurements = [int(x) for x in file_measurements.readlines()]

        result_task_one = self.check_depth_increase(measurements)
        print("Result Task 1: {}".format(result_task_one))

        result_task_two = self.check_three_measurements(measurements)
        print("Result Task 2: {}".format(result_task_two))

    
    def check_three_measurements(self, measurements):
        sliding_window = self.create_sliding_window(measurements)
        combined_measurements = self.replace_all_sliding_windows_with_sum(sliding_window)
        result = self.check_depth_increase(combined_measurements)
        return result


    def check_depth_increase(self, measurements):
        increase_counter = 0
        for i in range(1, len(measurements)):
            if (measurements[i - 1] < measurements[i]):
                increase_counter += 1
        return increase_counter

    def create_sliding_window(self, measurements):
        sliding_window = [measurements[x : x + 3] for x in range(0, len(measurements), 1)]
        return sliding_window

    def check_depth_of_sliding_window(self, sliding_window):
        return sum(sliding_window)

    def replace_all_sliding_windows_with_sum(self, sliding_windows):
        result = []
        for sliding_window in sliding_windows:
            result.append(self.check_depth_of_sliding_window(sliding_window))
        return result


class Tests(unittest.TestCase):

    def setUp(self):
        self.ship = Ship() 


    def test_depth_increases_in_small_list(self):
        input = [1,2]
        expected = 1
        actual = self.ship.check_depth_increase(input)
        self.assertEqual(expected, actual)


    def test_depth_increase_always_in_bigger_list(self):
        input = [1,2,3]
        expected = 2
        actual = self.ship.check_depth_increase(input)
        self.assertEqual(expected, actual)


    def test_depth_does_not_always_increase(self):
        input = [10, 20, 15, 18, 20]
        expected = 3
        actual = self.ship.check_depth_increase(input)
        self.assertEqual(expected, actual)


    def test_depth_does_not_increase(self):
        input = [90, 80, 78, 60, 23, 11]
        expected = 0
        actual = self.ship.check_depth_increase(input)
        self.assertEqual(expected, actual)


    def test_create_sliding_window_small_input(self):
        input = [1, 2, 3]
        expected = [[1, 2, 3], [2, 3], [3]]
        actual = self.ship.create_sliding_window(input)
        self.assertEqual(expected, actual)


    def test_create_sliding_window_two_measurements_sets(self):
        input = [1, 2, 3, 4]
        expected = [[1, 2, 3], [2, 3, 4], [3, 4], [4]]
        actual = self.ship.create_sliding_window(input)
        self.assertEqual(expected, actual)

    def test_check_depth_of_single_sliding_window(self):
        input = [1, 2, 3]
        expected = 6
        actual = self.ship.check_depth_of_sliding_window(input)
        self.assertEqual(expected, actual)


    def test_replace_sliding_window_with_sum(self):
        input = [[1, 2, 3]]
        expected = [6]
        actual = self.ship.replace_all_sliding_windows_with_sum(input)
        self.assertEqual(expected, actual)

    def test_replace_two_sliding_window_with_sum(self):
        input = [[1, 2, 3], [4, 5, 6]]
        expected = [6, 15]
        actual = self.ship.replace_all_sliding_windows_with_sum(input)
        self.assertEqual(expected, actual)

    def test_check_three_measurements(self):
        input = [1, 2, 3, 4, 5, 6]
        expected = 3
        actual = self.ship.check_three_measurements(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    ship = Ship()
    ship.main()
    unittest.main()
