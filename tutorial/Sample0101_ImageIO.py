# -*- coding: utf-8 -*-

import scipy.misc
import pylab

import PIL.Image

def LoadImage(iFilename):
    imgRGB = scipy.misc.imread(iFilename)
    return scipy.misc.imread(iFilename)

def SaveImage(oFilename, img, fmt=None):
    scipy.misc.imsave(oFilename, img, fmt)


def LoadImagePIL(iFilename, gray=False):
    if gray == True:
        return PIL.Image.open(iFilename).convert('L')
    else:
        return PIL.Image.open(iFilename)

def SaveImagePIL(oFilename, img):
    img.save(oFilename)

if __name__ == "__main__":
    iFilename = '../data/lena.jpg'
    oFilename = '/tmp/test.jpg'

    # Load
    img = LoadImage(iFilename)
    imgRGB = LoadImagePIL(iFilename)
    imgGray = LoadImagePIL(iFilename, gray=True)
    
    # Save
    SaveImage(oFilename, img)

    # show
    pylab.imshow(img)
    pylab.imshow(imgRGB)
    pylab.imshow(imgGray)
    
