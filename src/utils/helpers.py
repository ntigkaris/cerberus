import pathlib

import cv2

from conf.config import cfg

def takeSnapshot(imageSize,kernel):
    caption = cv2.VideoCapture(index=0)
    _,image = caption.read()
    image = cv2.cvtColor(src=image,
                        code=cv2.COLOR_BGR2GRAY)
    image = cv2.resize(src=image,
                    dsize=(imageSize,imageSize),
                    fx=0,fy=0,
                    interpolation=cv2.INTER_AREA)
    image = cv2.filter2D(src=image,
                        ddepth=-1,
                        kernel=kernel)
    cv2.imwrite(filename=f'{cfg.imgdir}/IMG_{cfg.timestamp}.png',
                img=image)
    pass

def logContents(query):
    targetDirectory = pathlib.Path(f'{pathlib.Path.home()}\\{query}')
    with open(file=f'{cfg.logdir}/LOG_{cfg.timestamp}.log',mode='a') as f:
        for path in targetDirectory.rglob(pattern='*'):
            f.write(f'{path.__str__()}\n')
    pass
