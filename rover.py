import os

cardinal_to_angle = {0: "E", 90: "N", 180: "W", 270: "S"}
angle_to_cardinal = {"E": 0, "N": 90, "W": 180, "S": 270}
moves = {0: {"x": 1, "y": 0}, 90: {"x": 0, "y": 1}, 180: {"x": -1, "y": 0}, 270: {"x": 0, "y": -1}}


class Rover:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y

    def rotate(self, angle):
        self.direction += angle

        if self.direction == 360:
            self.direction = 0
        elif self.direction < 0:
            self.direction = 360 - abs(self.direction)

    def move(self, boundry_x, boundry_y):
        if 0 <= self.x + moves[self.direction]['x'] <= boundry_x:
            self.x += moves[self.direction]['x']
        if 0 <= self.y + moves[self.direction]['y'] <= boundry_y:
            self.y += moves[self.direction]['y']

    def get_location(self):
        return f"{self.x} {self.y} {cardinal_to_angle[self.direction]}"


def get_inputs():
    filename = "demofile.txt"
    if os.path.getsize(filename) == 0:
        print("Empty File")
        return

    with open(filename, "r") as f:
        for count, line in enumerate(f):
            line = line.rstrip('\n')
            if count == 0:
                boundry_x = int(line[0])
                boundry_y = int(line[1])
            elif count == 1:
                initial_loc = line.split(" ")
                initial_loc_x = int(initial_loc[0][0])
                initial_loc_y = int(initial_loc[0][1])
                initial_loc_direction = initial_loc[1]
            elif count == 2:
                commands = line
    return boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands


def run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands):
    rover = Rover(angle_to_cardinal[initial_loc_direction], initial_loc_x, initial_loc_y)
    for command in commands:
        if command == "M":
            rover.move(boundry_x, boundry_y)
        elif command == "R":
            rover.rotate(-90)
        elif command == "L":
            rover.rotate(90)
    return rover.get_location()


if __name__ == "__main__":
    boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands = get_inputs()
    resultant_loc = run(boundry_x, boundry_y, initial_loc_x, initial_loc_y, initial_loc_direction, commands)
    print(resultant_loc)
