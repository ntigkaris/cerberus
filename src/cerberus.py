from utils.helpers import takeSnapshot,logContents
from conf.config import cfg

if __name__=='__main__':
    takeSnapshot(imageSize=cfg.imgsize,kernel=cfg.kernel)
    logContents(query=cfg.tgtdir)
