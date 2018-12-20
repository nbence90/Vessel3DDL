import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser()

parser.add_argument('--rascoordfile',help='directory to DICOM folder ')
parser.add_argument('--mhdfile',help='mhd contains the transformation matrix ')

args = parser.parse_args()

raspath = args.rascoordfile

df = pd.read_csv(raspath)



