from datetime import datetime

import numpy as np

class cfg:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    imgdir = '../data/captions'
    recdir = '../data/snapshots'
    tmpdir = '../data/temp'
    imgsize = 256
    kernel = np.array([[-1,-1,-1],
                       [-1,9,-1],
                       [-1,-1,-1]])
