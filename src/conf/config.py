from datetime import datetime

import numpy as np

class cfg:
    """
    Attributes:
    filename
    cleanup
    imgdir
    recdir
    tmpdir
    rectype
    imgtype
    imgsize
    kernel

    Methods:
    
    Description:
    Core configuration class
    """
    filename = datetime.now().strftime('%Y%m%d%H%M%S')
    cleanup = 7
    imgdir = '../data/captions'
    recdir = '../data/snapshots'
    tmpdir = '../data/temp'
    rectype = 'txt'
    imgtype = 'jpg'
    imgsize = 256
    kernel = np.array([[-1,-1,-1],
                       [-1,9,-1],
                       [-1,-1,-1]])
