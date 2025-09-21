def openMaze (filename) :
    fileInp = open(f"maps/{filename}", "r")
    maze = []
    for line in fileInp.readlines() :
        newLine = list(line.replace("\n",""))
        maze.append(newLine)
    fileInp.close()
    return maze

def printMaze (maze) :
    for line in maze :
        print(line)

def findEnds(maze) :
    start = None
    goal = None
    DIRS = [(-1,0),(1,0),(0,1),(0,-1)] #Up, Down, Left, Right
    for y in range(len(maze)) :
        for x in range(len(maze[0])) :
            if (maze[y][x] == "S") :
                start = (y,x)
            elif (maze[y][x] == "G") :
                goal = (y,x)
    return start, goal

def buildPath(parents, goal) :
    path = []
    current = goal
    while current in parents :
        path.append(current)
        cur = parents[cur]
    return path[::-1]
