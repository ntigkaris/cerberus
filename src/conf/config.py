from datetime import datetime

import numpy as np

class cfg:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    imgdir = '../data/captions'
    recdir = '../data/snapshots'
    tgtdir = 'Downloads'
    imgsize = 128
    kernel = np.array([[-1,-1,-1],
                       [-1,9,-1],
                       [-1,-1,-1]])
