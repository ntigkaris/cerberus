import os

from conf.config import cfg

os.makedirs(name=cfg.imgdir,exist_ok=True)
os.makedirs(name=cfg.recdir,exist_ok=True)
os.makedirs(name=cfg.tmpdir,exist_ok=True)
