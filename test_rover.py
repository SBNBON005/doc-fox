import unittest
import rover


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        boundry_x = 8
        boundry_y = 8
        initial_loc_x = 1
        initial_loc_y = 2
        initial_loc_direction = "E"
        commands = "MMLMRMMRRMML"

        expected_results = "3 3 S"
        actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
        self.assertEqual(actual_results, expected_results)

    def test_case_two(self):
        boundry_x = 8
        boundry_y = 2
        initial_loc_x = 0
        initial_loc_y = 2
        initial_loc_direction = "S"
        commands = "MMMM"

        expected_results = "0 0 S"
        actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
        self.assertEqual(actual_results, expected_results)

    def test_case_three(self):
        boundry_x = 8
        boundry_y = 2
        initial_loc_x = 0
        initial_loc_y = 2
        initial_loc_direction = "N"
        commands = "MMMM"

        expected_results = "0 2 N"
        actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
        self.assertEqual(actual_results, expected_results)

    def test_case_four(self):
        boundry_x = 8
        boundry_y = 8
        initial_loc_x = 0
        initial_loc_y = 0
        initial_loc_direction = "E"
        commands = "MMLMM"

        expected_results = "2 2 N"
        actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
        self.assertEqual(actual_results, expected_results)

    def test_case_five(self):
        boundry_x = 0
        boundry_y = 0
        initial_loc_x = 0
        initial_loc_y = 0
        initial_loc_direction = "E"
        commands = "MMLMM"

        expected_results = "0 0 N"
        actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
        self.assertEqual(actual_results, expected_results)

    def test_case_six(self):
        boundry_x = 0
        boundry_y = 0
        initial_loc_x = 0
        initial_loc_y = 0
        initial_loc_direction = "E"
        commands = "MMLMM"

        expected_results = "0 0 N"
        actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
        self.assertEqual(actual_results, expected_results)

    def test_case_seven(self):
        boundry_x = 0
        boundry_y = 0
        initial_loc_x = 0
        initial_loc_y = 0
        initial_loc_direction = "E"
        commands = "LLLL"

        expected_results = "0 0 E"
        actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
        self.assertEqual(actual_results, expected_results)

    def test_case_eight(self):
        boundry_x = 0
        boundry_y = 0
        initial_loc_x = 0
        initial_loc_y = 0
        initial_loc_direction = "E"
        commands = "RRRRRRRR"

        expected_results = "0 0 E"
        actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
        self.assertEqual(actual_results, expected_results)


if __name__ == '__main__':
    unittest.main()
