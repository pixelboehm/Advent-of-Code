import unittest

class CalculateFuel():

    def main(self):
        required_fuel = 0
        with open("input_day01.txt") as fp:
            for value in fp.readlines():
                required_fuel += self.calculate_fuel(int(value))
        print(required_fuel)


    def calculate_fuel(number):
        fuel = (number // 3) - 2
        return fuel

class Tests(unittest.TestCase):

    def test_numberIsMultipleOfThree(self):
        fuel = CalculateFuel.calculate_fuel(9)
        self.assertEqual(fuel, 1)

    def test_numberIsNotMultipleOfThree(self):
        fuel = CalculateFuel.calculate_fuel(10)
        self.assertEqual(fuel, 1)

    def test_bigNumber(self):
        fuel = CalculateFuel.calculate_fuel(127296)
        self.assertEqual(fuel, 42430)


if __name__ == '__main__':
    # unittest.main()
    CalculateFuel.main(CalculateFuel)
