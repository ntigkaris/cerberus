import os
import datetime
import pathlib
import shutil

import cv2

from conf.config import cfg

def cleanUp(oldDir,fileType):
    """
    Parameters:
    oldDir : str; absolute or relative directory path
    fileType: str; generated file extension
    
    Returns:
    
    Description:
    Takes an absolute or relative directory path and archives past created files, grouping them by creation date. The retention period is specified by configuration parameter cfg.cleanup
    """
    oldIds = [(datetime.date.today()-datetime.timedelta(days=i+1)).strftime('%Y%m%d') for i in range(cfg.cleanup)]
    for id in oldIds:
        os.makedirs(name=cfg.tmpdir,exist_ok=True)
        for path in pathlib.Path(oldDir).rglob(pattern=f'*{id}*{fileType}'):
            os.rename(src=path.__str__(),
                      dst=path.__str__().replace('\\','/')\
                                        .replace(oldDir,cfg.tmpdir))
        if len(os.listdir(path=cfg.tmpdir)): shutil.make_archive(base_name=f'{oldDir}/{id}',
                                                                 format='zip',
                                                                 root_dir=cfg.tmpdir)
        shutil.rmtree(path=cfg.tmpdir)
    pass

def takeCaption():
    """
    Parameters:
    
    Returns:
    
    Description:
    Applies directory clean-up. Captures an image using the device's camera. Resizes image to size specified by cfg.imgsize. Applies a kernel transformation specified by cfg.kernel. Image type is specified by cfg.imgtype
    """
    cleanUp(oldDir=cfg.imgdir,
            fileType=cfg.imgtype)
    caption = cv2.VideoCapture(index=0)
    _,image = caption.read()
    image = cv2.cvtColor(src=image,
                         code=cv2.COLOR_BGR2GRAY)
    image = cv2.resize(src=image,
                       dsize=(cfg.imgsize,cfg.imgsize),
                       fx=0,
                       fy=0,
                       interpolation=cv2.INTER_AREA)
    image = cv2.filter2D(src=image,
                         ddepth=-1,
                         kernel=cfg.kernel)
    cv2.imwrite(filename=f'{cfg.imgdir}/{cfg.timestamp}.{cfg.imgtype}',
                img=image)
    pass

def logHomeContents():
    """
    Parameters:
    
    Returns:
    
    Description:
    Applies directory clean-up. Writes Home directory contents into a file, whose type is specified by cfg.rectype
    """
    cleanUp(oldDir=cfg.recdir,
            fileType=cfg.rectype)
    with open(file=f'{cfg.recdir}/{cfg.timestamp}.{cfg.rectype}',
              mode='w',
              encoding='utf8') as f:
        for path in pathlib.Path.home().rglob(pattern='*'):
            f.write(f'{path.__str__()}\n')
    pass
