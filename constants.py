DIMENTIONS = (20, 32)
DIMENTIONS = (10, 16)
# DIMENTIONS = (5, 8)
TOTALSQUARES = DIMENTIONS[0]*DIMENTIONS[1]


RATIO = 0.075
MINRATIO, MAXRATIO = [RATIO/1.25, RATIO*1.25]

ORIGINSRANGE  = [int(TOTALSQUARES*MINRATIO), int(TOTALSQUARES*MAXRATIO)]

SQUAREWIDTH = 32
SQUAREHEIGHT = 32
MARGIN = 32

TOTALWIDTH = DIMENTIONS[0]*SQUAREWIDTH+2*MARGIN
TOTALHEIGHT = DIMENTIONS[1]*SQUAREHEIGHT+2*MARGIN
SCREENSIZE = (TOTALHEIGHT,TOTALWIDTH)


# ORIGIN = 1
PATH  =2
WALL = 1
NOTHING = 0
NODE = 3

UP = [-1,0]
DOWN = [1,0]
LEFT = [0, -1]
RIGHT = [0, 1]
STOP = [0,0]