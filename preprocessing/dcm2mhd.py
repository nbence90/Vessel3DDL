import os
import sys
import SimpleITK as sitk
import argparse

"""
python2 dcm2mhd.py 
--inputdir '/media/bence/Elements1/Databases/IRCAD/3Dircadb1/3Dircadb1.4/MASKS_DICOM/liver/' 
--outputfilepath /media/bence/Elements1/Databases/IRCAD/3Dircadb1/VESSEL/VESSEL12_01-20_Livermasks/VESSEL12_04.mhd
"""
parser = argparse.ArgumentParser()
parser.add_argument('--inputdir',help='directory to DICOM folder ')
parser.add_argument('--outputfilepath',help='directory to DICOM folder ')

args = parser.parse_args()

dirname = args.inputdir
outputfilepath = args.outputfilepath

series_IDs = sitk.ImageSeriesReader_GetGDCMSeriesIDs(dirname)

if not series_IDs:
  print('No series in directory ' + '\'' + dirname + '\'')

# Write mhd into the same directory as dicom file
for series in series_IDs:
  if args.outputfilepath is not None:
    filename = outputfilepath
  elif args.inputdir is not None:
    outputfilepath = os.path.join(dirname, series + '.mhd')
  else:
    outputfilepath = series + '.mhd'
  sitk.WriteImage(sitk.ReadImage(sitk.ImageSeriesReader_GetGDCMSeriesFileNames(dirname, series)), filename)
