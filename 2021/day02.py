import unittest

class Boat():

    def main(self):
        position = {
            'forward': 0,
            'up': 0,
            'down': 0,
            'aim': 0,
        }
        commands = []
        with open("input_day02.txt") as fp:
            for entry in fp.readlines():
                commands.append(entry.rstrip("\n"))         
        result_task_one = self.multiply_final_horizontal_position_with_depth(commands, position)
        print(result_task_one)


    def get_coordinates(self, coordinates):
        direction = coordinates[:coordinates.index(" ")]
        value = int(coordinates[coordinates.index(" "):])
        return direction, value

    def add_coordinates_to_position(self, position, direction, value):
        position[direction] += value
        return position


    def get_final_coordinates(self, commands, position):
        for entry in commands:
            direction, value = self.get_coordinates(entry)
            position = self.add_coordinates_to_position(position, direction, value)
        return position


    def calculate_depth(self, position):
        return position['down'] - position['up']


    def multiply_final_horizontal_position_with_depth(self, commands, position):
        position = self.get_final_coordinates(commands, position)
        return position['forward'] * self.calculate_depth(position)
            


class Tests(unittest.TestCase):

    def setUp(self):
        self.boat = Boat() 
        self.position = {
            'forward': 0,
            'up': 0,
            'down': 0,
            'aim': 0
        }


    def test_get_coordinates(self):
        input = 'forward 3'
        expected_direction, expected_value = self.boat.get_coordinates(input)
        self.assertEqual(expected_direction, 'forward')
        self.assertEqual(expected_value, 3)


    def test_add_forward_coordinates_to_position(self):
        direction = 'forward'
        value = 5
        expected = {
            'forward': 5,
            'up': 0,
            'down': 0,
            'aim': 0,
        }
        actual = self.boat.add_coordinates_to_position(self.position, direction, value)
        self.assertEqual(expected, actual)


    def test_add_up_coordinates_to_position(self):
        direction = 'up'
        value = 3
        expected = {
            'forward': 0,
            'up': 3,
            'down': 0,
            'aim': 0
        }
        actual = self.boat.add_coordinates_to_position(self.position, direction, value)
        self.assertEqual(expected, actual)


    def test_get_final_position(self):
        expected = {
            'forward': 1,
            'up': 2,
            "down": 3,
            "aim": 0,
        }
        actual = self.boat.get_final_coordinates(['forward 1', 'up 2', 'down 3'], self.position)
        self.assertEqual(expected, actual)


    def test_calculate_depth(self):
        input = {
            'forward': 1,
            'up': 2,
            "down": 3,
            "aim": 0,
        }
        expected = 1
        actual = self.boat.calculate_depth(input)
        self.assertEqual(expected, actual)


    def test_calculate_final_position(self): 
        input = ['forward 1', 'forward 1', 'down 3', 'up 2', 'down 2']
        expected = 6
        actual = self.boat.multiply_final_horizontal_position_with_depth(input, self.position)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    boat = Boat()
    boat.main()
    unittest.main()