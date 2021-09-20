import cv2 as cv
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True , help="name of the input")
args = vars(ap.parse_args())

img = cv.imread(args["input"])

cv.imshow('cat', img)

cv.waitKey(0)