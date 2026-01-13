from datetime import datetime

import numpy as np

class cfg:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    imgdir = '../data/captions'
    recdir = '../data/snapshots'
    imgfilename = f'IMG{timestamp}.png'
    recfilename = f'REC{timestamp}.txt'
    imgsize = 128
    kernel = np.array([[-1,-1,-1],
                       [-1,9,-1],
                       [-1,-1,-1]])
