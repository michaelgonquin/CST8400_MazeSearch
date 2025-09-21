import maphelper

def depthSearch(maze, pos, path, solved) :
    openSpaces = maphelper.neighbors(maze, pos)
    nextPos = pos
    if (openSpaces["U"]) :
        nextPos["y"] -= 1
        nextPath = path[:].append(nextPos)
        if (maphelper.checkSolved(maze, nextPos)) :
            return nextPath
        depthSearch(maze, nextPos, nextPath)
    if (openSpaces["D"]) :
        nextPos["y"] += 1
        nextPath = path[:].append(nextPos)
        depthSearch(maze, nextPos, nextPath)
    if (openSpaces["L"]) :
        nextPos["x"] -= 1
        nextPath = path[:].append(nextPos)
        depthSearch(maze, nextPos, nextPath)
    if (openSpaces["R"]) :
        nextPos["x"] += 1
        nextPath = path[:].append(nextPos)
        depthSearch(maze, nextPos, nextPath)