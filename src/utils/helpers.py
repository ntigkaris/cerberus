import os
import datetime
import pathlib
import shutil

import cv2

from conf.config import cfg

def cleanUp(oldDir):
    os.makedirs(name=cfg.tmpdir,exist_ok=True)
    oldID = (datetime.date.today()-datetime.timedelta(days=1)).strftime('%Y%m%d')
    for path in pathlib.Path(oldDir).rglob(pattern=f'*{oldID}*'):
        os.rename(src=path.__str__(),
                  dst=path.__str__().replace('\\','/')\
                                    .replace(oldDir,cfg.tmpdir))
    if len(os.listdir(path=cfg.tmpdir)): shutil.make_archive(base_name=f'{oldDir}/{oldID}',
                                                             format='zip',
                                                             root_dir=cfg.tmpdir)
    shutil.rmtree(path=cfg.tmpdir)
    pass

def takeCaption():
    cleanUp(cfg.imgdir)
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
    cv2.imwrite(filename=f'{cfg.imgdir}/{cfg.timestamp}.png',
                img=image)
    pass
    
def logHomeContents():
    cleanUp(cfg.recdir)
    with open(file=f'{cfg.recdir}/{cfg.timestamp}.txt',
              mode='w',
              encoding='utf8') as f:
        for path in pathlib.Path.home().rglob(pattern='*'):
            f.write(f'{path.__str__()}\n')
    pass
