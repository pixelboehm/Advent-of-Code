import unittest

## Need to start over again, because the input needs to be read in sequence and not in total

class Boat():

    def main(self):
        position = {
            'forward': 0,
            'depth': 0,
            'up': 0,
            'down': 0,
            'aim': 0,
        }
        commands = []
        with open("input_day02.txt") as fp:
            for entry in fp.readlines():
                commands.append(entry.rstrip("\n"))         
                direction, value = self.get_coordinates(entry.rstrip("\n"))

                if direction == "forward":
                    position["forward"] += value
                    position["depth"] += position["aim"] * value 
                elif direction == "up":
                    position["aim"] -= value
                elif direction == "down":
                    position["aim"] += value
                else:
                    print("Unknown Direction")

            result_task2 = position["forward"] * position["depth"]
            print(result_task2)


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
            
    def calculate_aim(self, position):
        position['aim'] = position['down'] - position['up']
        return position

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


if __name__ == '__main__':
    boat = Boat()
    boat.main()
    unittest.main()