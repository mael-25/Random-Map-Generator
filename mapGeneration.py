import random

import numpy as np
from constants import *
import logging
from generateRandomSeed import getSeed

IMPORTANTINFO = 35
logging.addLevelName(IMPORTANTINFO, "INFO")


def generate_map(seed=-1):

    logger = logging.getLogger("Maze Generation Logger")

    seed = getSeed(seed)
    random.seed(seed)

    logger.info("Seed: ({})".format(seed))
    logger.log(IMPORTANTINFO, "Seed: ({})".format(seed))

    origins_random_number = True


    if origins_random_number:
        origins = random.randint(ORIGINSRANGE[0], ORIGINSRANGE[1])
        logger.info("Random number of origins ({})".format(origins))
    else:
        origins = int(RATIO*TOTALSQUARES)
        logger.info("Set number of origins ({})".format(origins))


    grid = np.zeros((DIMENTIONS[0]-2, DIMENTIONS[1]-2), dtype=np.int16)

    total_origins_added = 0

    origins_list = []

    current_id = 2

    unsucessfullTries = 0

    logger.info("Generating Origins")
    while total_origins_added < origins:
        candidate_pos = (random.randrange(0, DIMENTIONS[0]-2),
                        random.randrange(0, DIMENTIONS[1]-2))
        unallowed_pos = [(x, y) for x in range(candidate_pos[0]-1, candidate_pos[0]+2)
                                for y in range(candidate_pos[1]-1, candidate_pos[1]+2)]
        point_accepted = True
        for x, id in origins_list:
            if x in unallowed_pos:
                point_accepted = False
                break
            else:
                pass
        unsucessfullTries += 1
        if point_accepted:
            logger.debug(f"{current_id-1}th point accepted")
            origins_list.append([candidate_pos, current_id])
            grid[candidate_pos] = current_id
            total_origins_added += 1
            current_id += 1
            unsucessfullTries = 0
        if unsucessfullTries == 20:
            logger.warn("Has 20 consecutive unsucessfull tries")
        if unsucessfullTries >= 100:
            # logging.addLevelName()
            logger.error("Has 100 consecutive unsucessfull tries, aborting. Seed: {}".format(seed))
            ValueError("Bad Seed")


    # print(grid)

    total_id = current_id

    finished = False
    turn = 1

    while not finished:
        random.shuffle(origins_list)
        propagated_this_time = False
        for origin, id in origins_list:
            # to_add = [(x, y) for x in [origin[0]-turn, origin[0], origin[0]+turn]
            #                     for y in [origin[1]-turn, origin[1], origin[1]+turn]]

            to_add = [(x, y) for x in range(origin[0]-turn, origin[0]+turn+1) for y in [origin[1]-turn, origin[1]+turn]]
            to_add+=[(x, y) for x in [origin[0]-turn, origin[0]+turn] for y in range(origin[1]-turn+1, origin[1]+turn)]
            # del to_add[4] # (origin[0], origin[1])
            to_del = []
            # if id == 16:
            #     print(16)
            for point in to_add:
                if (point[0] >= len(grid) or point[1] >= len(grid[0])) or (point[0] < 0 or point[1] < 0): 
                    to_del.append(point)
            for x in to_del:
                del to_add[to_add.index(x)]

            for point in to_add:
                abort_if_wall_at_pos = [(x, y) for x in range(point[0]-1, point[0]+2)
                                        for y in range(point[1]-1, point[1]+2)]
                # del abort_if_wall_at_pos[4]
                # if point ==(0,0):
                #     print((0,0))
                
                success = True
                for x in abort_if_wall_at_pos:
                    if (x[0] < len(grid) and x[1] < len(grid[0])) and (x[0] >= 0 and x[1] >= 0):
                        if grid[x] != 0:
                            if grid[x] != total_id+id and grid[x] != id:
                                success = False
                                break
                        else:
                            pass
                if success:
                    grid[point] = total_id+id

                    propagated_this_time = True

        if not propagated_this_time:
            finished = True

        turn += 1

    # print(grid)
    final_grid = np.zeros(DIMENTIONS, np.int16)
    final_grid[1:DIMENTIONS[0]-1,1:DIMENTIONS[1]-1] = grid
    # print(final_grid)

    logger.info(f"{turn-2} turn(s)")

    final_grid2 = np.zeros(DIMENTIONS, dtype=np.int0)
    # final_grid2[1,5] = 1
    # print(final_grid2)

    for i, x in enumerate(final_grid):
        for i2, y in enumerate(final_grid[i]):
            final_grid2[i, i2] = int(bool(y))

    return final_grid2

if __name__ == "__main__":
    level = logging.INFO
    logging.basicConfig(format='%(levelname)s - %(name)s - %(message)s', level=level)
    print(generate_map())