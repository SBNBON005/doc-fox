import rover


def test_case_one():
    boundry_x = 8
    boundry_y = 8
    initial_loc_x = 1
    initial_loc_y = 2
    initial_loc_direction = "E"
    commands = "MMLMRMMRRMML"

    expected_results = "3 3 S"
    actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
    assert actual_results == expected_results


def test_case_two():
    boundry_x = 8
    boundry_y = 2
    initial_loc_x = 0
    initial_loc_y = 2
    initial_loc_direction = "S"
    commands = "MMMM"

    expected_results = "0 0 S"
    actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
    assert actual_results == expected_results


def test_case_three():
    boundry_x = 8
    boundry_y = 2
    initial_loc_x = 0
    initial_loc_y = 2
    initial_loc_direction = "N"
    commands = "MMMM"

    expected_results = "0 2 N"
    actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
    assert actual_results == expected_results


def test_case_four():
    boundry_x = 8
    boundry_y = 8
    initial_loc_x = 0
    initial_loc_y = 0
    initial_loc_direction = "E"
    commands = "MMLMM"

    expected_results = "2 2 N"
    actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
    assert actual_results == expected_results


def test_case_five():
    boundry_x = 0
    boundry_y = 0
    initial_loc_x = 0
    initial_loc_y = 0
    initial_loc_direction = "E"
    commands = "MMLMM"

    expected_results = "0 0 N"
    actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
    assert actual_results == expected_results


def test_case_six():
    boundry_x = 0
    boundry_y = 0
    initial_loc_x = 0
    initial_loc_y = 0
    initial_loc_direction = "E"
    commands = "MMLMM"

    expected_results = "0 0 N"
    actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
    assert actual_results == expected_results


def test_case_seven():
    boundry_x = 0
    boundry_y = 0
    initial_loc_x = 0
    initial_loc_y = 0
    initial_loc_direction = "E"
    commands = "LLLL"

    expected_results = "0 0 E"
    actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
    assert actual_results == expected_results


def test_case_eight():
    boundry_x = 0
    boundry_y = 0
    initial_loc_x = 0
    initial_loc_y = 0
    initial_loc_direction = "E"
    commands = "RRRRRRRR"

    expected_results = "0 0 E"
    actual_results = rover.run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
    assert actual_results == expected_results


def test_case_nine():
    filename = "demofile.txt"
    expected_results = (8, 8, 1, 2, "E", "MMLMRMMRRMML")
    actual_results = rover.get_inputs(filename)
    assert actual_results == expected_results


def test_case_ten():
    filename = "empty_file"
    expected_results = None
    actual_results = rover.get_inputs(filename)
    assert actual_results == expected_results
