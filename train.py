import os.path as osp

import archs  # noqa: F401
import data  # noqa: F401
import models  # noqa: F401
from basicsr.train import train_pipeline

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir))
    print('aa')
    print('bb')
    print('cc')
    print('dd')
    print('ee')
    print('ff')
    print('gg')
    print('hh')

    print('jj')
    print('kk')
    print('ll')
    print('mm')
    print('nn')
    train_pipeline(root_path)
