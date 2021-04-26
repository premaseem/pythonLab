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

def solution(grid_max_x, grid_max_y, initial_position, commands):
    return ""




print(solution(5, 5, "1 2 N", ["R", "M", "L", "M", "R"])) # output "2 3 E"
print(solution(5, 5, "1 2 N", ["L", "M", "L", "M", "L", "M", "L", "M", "M"])) # output "1 3 N"
print(solution(5, 5, "1 4 N", ["L", "M", "M", "M", "L", "M", "R"])) # output "0 3 W"




























