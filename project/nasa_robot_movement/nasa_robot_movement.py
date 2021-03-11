"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

"""
# NASA is sending a robot to Moon's surface in an unmanned mission. The robot will be controlled remotely by issuing simple commands to maneuver it.

# The robot's position is represented by a combination of an x and y co-ordinates and a letter representing one of the four directions in which it is facing. An example position might be 0, 0, N, which means the robot is in the bottom left corner and facing North.

# Directions Key: E = East, W = West, S = South, N = North

# Grid : 0,0 is at bottom left.

# ........................(+x,+y)
# |                         |
# |                         |
# 0,0 ......................|


# Nasa sends commands in the form of simple letters. L, R and.

# L : Rotates the robot 90 degrees Counter-clockwise in it's current position itself
# R : Rotates the robot 90 degrees clockwise in it's current position itself
# M : Moves the robot 1 unit forward in whatever direction it is facing

# Important NOTE: The robot will stay in its position if you try to move beyond any edge of the grid

# INPUT:

# (max-X-coordinate, max-Y-coordinate, current-position-and-direction, [list of commands])

# Example: solution(5, 5, "1 2 N", ["R", "M", "L", "M", "R"])

# The grid goes from (0,0 to 5,5)

###### Example for (5,5) grid:

# 0,5  1,5  2,5  3,5  4,5  5,5

# 0,4  1,4  2,4  3,4  4,4  5,4

# 0,3  1,3  2,3  3,3  4,3  5,3

# 0,2  1,2  2,2  3,2  4,2  5,2

# 0,1  1,1  2,1  3,1  4,1  5,1

# 0,0  1,0  2,0  3,0  4,0  5,0


######  Directions for reference

#              N
#              |
#              |
#       W ----- ----- E
#              |
#              |
#              S

# EXPECTED OUTPUT:

# Final position and direction of the robot (X, Y, Direction) as a string

# Example: "2 3 E"

# Explanation:

# Initial position: 1,2,N
# R : Turn Right to point in East direction
# M : Move 1 grid point to 2,2
# L : Turn Left to point in North direction
# M : Move 1 grid point to 2, 3
# R : Turn Right to point in East direction
# Final Position: 2 3 E




# --------------------- Python -------------------

def sol(grid_max_x, grid_max_y, initial_position, commands):
    sp = initial_position.split(" ")
    x = int(sp[0])
    y = int(sp[1])
    p = sp[2]

    pm = {}
    pm["N"] = [0,1]
    pm["S"] = [0,-1]
    pm["E"] = [1,0]
    pm["W"] = [-1,0]

    d = ["N","E","S","W"]
    cd = d.index(p)
    for c in commands:
        cd = d.index(d[cd])

        if c == "L":
            cd = cd - 1
            if cd < 0:
                cd = 3

        elif c == "R":
            cd = cd + 1
            if cd > 3:
                cd = 0

        else:

            delta = pm.get(d[cd])
            if x < grid_max_x:
                x = x + delta[0]
                if x == -1 :
                    x = 0
            if y < grid_max_y and y >= 0 :
                y = y + delta[1]
                if y == -1:
                    y = 0

    # print("output", x,y,d[cd])

    return "{} {} {}".format(str(x),str(y),str(d[cd]))


test_data = [
    ((5, 5, "1 2 N", ["R", "M", "L", "M", "R"]), "2 3 E"),
    ( (5, 5, "1 2 N", ["L", "M", "L", "M", "L", "M", "L", "M", "M"] ), "1 3 N"),
    ( (5, 5, "1 4 N", ["L", "M", "M", "M", "L", "M", "R"] ), "0 3 W"),
]

for given, expected in test_data:
    print(f" Test with given {given} and expected = {expected}", end=" == ")
    actual = sol(*given)
    print("actual", sol(*given))
    assert actual == expected
