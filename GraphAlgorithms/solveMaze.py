def isSafeMove(pos_x, pos_y, len, height, visited_arr):
    if (
            pos_x >= 0 and pos_x < len
            and pos_y >= 0 and pos_y < height
            and not visited_arr[pos_x][pos_y]
        ):
        return True

    return False

def solveMaze(maze, target_x, target_y, start_x, start_y, visited_arr):

    if not maze[start_x][start_y]:
        return False
    
    visited_arr[start_x][start_y] = 1

    if start_x == target_x and start_y == target_y:
        return True
    
    direction_x = [0, 0, 1, -1]
    direction_y = [-1, 1, 0, 0]
    loop_res = False

    for i in range(4):
        safeMove = isSafeMove(
                        start_x + direction_x[i],
                        start_y + direction_y[i],
                        len(maze) - 1,
                        len(maze[start_x]) - 1,
                        visited_arr 
                    )
        if  safeMove:          
            solveM = solveMaze(
                                maze,
                                target_x,
                                target_y,
                                start_x + direction_x[i],
                                start_y + direction_y[i],
                                visited_arr
            )
            if  solveM:
                loop_res = True
                break

    if not loop_res:
        visited_arr[start_x][start_y] = 0
        return False

    return loop_res

def solveMazeExample():
    target_x = 2
    target_y = 0

    maze = [
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 1]
    ]

    visited_maze = [[0 for col in range(len(maze))] for row in range(len(maze[0]))]

    if solveMaze(maze, target_x, target_y, 0, 1, visited_maze):
        print(True)
    else:
        print(False)

    for i in range(len(maze)):
        print(visited_maze[i])

# solveMazeExample()



