# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 08:30:17 2016

@author: konopczynski
Visualize the output volume
"""

import numpy as np
import pyqtgraph as pg
import sys
#sys.path.append('./')
import config
import nibabel as nib
import os 

def main():
    param = config.read_parameters()
    path2save = param.path2Output
    fn = param.dictionaryName+'_'+param.outputFn
    z = np.load(path2save+fn)

    # save as nifti image
    #affine = np.eye(4)
    affine = np.diag([1, -1, -1, 1])
    array_img = nib.Nifti1Image(z, affine)

    nib.save(array_img, os.path.join(param.path2Output,  'output.nii'))

    pg.image(z)
    raw_input('click to end')
    

    return None

if __name__ == '__main__':
    main()
