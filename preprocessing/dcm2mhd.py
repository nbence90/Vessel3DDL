import os
import sys
import SimpleITK as sitk

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--dcmdir',help='directory to DICOM folder ')

args = parser.parse_args()

dirname = args.dcmdir

series_IDs = sitk.ImageSeriesReader_GetGDCMSeriesIDs(dirname)

if not series_IDs:
  print('No series in directory ' + '\'' + dirname + '\'')

# Write mhd into the same directory as dicom file
for series in series_IDs:
  sitk.WriteImage(sitk.ReadImage(sitk.ImageSeriesReader_GetGDCMSeriesFileNames(dirname, series)),
              os.path.join(dirname, series + '.mhd'))
