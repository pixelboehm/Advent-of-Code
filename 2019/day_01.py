import unittest

class CalculateFuel():

    def __init__(self):
        pass

    def main(self):
        required_fuel = 0
        self.elf = CalculateFuel()
        with open("input_day01.txt") as fp:
            for value in fp.readlines():
                required_fuel += self.elf.calculate_fuel_part2(int(value))
        print(required_fuel)


    def calculate_fuel(self, number):
        fuel = (number // 3) - 2
        return fuel

    def calculate_fuel_part2(self, number):
        fuel = self.calculate_fuel(number)
        if fuel <= 0:
            return 0
        return fuel+self.calculate_fuel_part2(fuel)

class Tests(unittest.TestCase):

    def setUp(self):
        self.elf = CalculateFuel()

    def test_numberIsMultipleOfThree(self):
        fuel = self.elf.calculate_fuel(9)
        self.assertEqual(fuel, 1)

    def test_numberIsNotMultipleOfThree(self):
        fuel = self.elf.calculate_fuel(10)
        self.assertEqual(fuel, 1)

    def test_bigNumber(self):
        fuel = self.elf.calculate_fuel(127296)
        self.assertEqual(fuel, 42430)

    def test_simpleNumber_part2(self):
        fuel = self.elf.calculate_fuel_part2(14)
        self.assertEqual(fuel, 2)

    def test_biggerNumber_part2(self):
        fuel = self.elf.calculate_fuel_part2(1969)
        self.assertEqual(fuel, 966)

    def test_evenBiggerNumber_part2(self):
        fuel = self.elf.calculate_fuel_part2(100756)
        self.assertEqual(fuel, 50346)


if __name__ == '__main__':
    # unittest.main()
    CalculateFuel.main(CalculateFuel)
