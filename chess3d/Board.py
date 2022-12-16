import numpy as np
from chess3d.Pieces import NONE, BLACK, WHITE

#
class Board:
    def __init__(self):
        array = np.zeros(shape=[8, 8, 8])

        # Fill with pawns
        for i in range(8):
            pass
            # array[]