from PIL import Image
import pylab

iFilename = '../data/lena.jpg'
imgRGB = Image.open(iFilename)
imgGray = Image.open(iFilename).convert('L')

pylab.imshow(imgRGB)
