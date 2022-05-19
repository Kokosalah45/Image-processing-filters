# %%
from re import S
from tkinter import Image

from imageio import read
import numpy as np
from matplotlib import pyplot as plt
from skimage.io import imread

# x = np.shape([[1,2],[3,4] ])

class PointProcessing:
    def __init__(self, img):
        self.img = img;
        x, y = img.shape
        self.imgX = x
        self.imgY = y

    def getImageDetails(self):
        return [self.imgX, self.imgY, self.img]

    def grayIntensity(self, k=1):
        rows, cols, img = self.getImageDetails()
        resImg = np.zeros((rows, cols))
        for row in range(0, rows):
            for col in range(0, cols):
                l = (2 ** k) - 1
                resImg[row][col] = img[row][col] % l
        return resImg

    def Sample(self, factor):
        rows, cols, img = self.getImageDetails()
        skipRateOfRows = rows // factor
        skipRateOfColumns = cols // factor

        resImg = np.zeros((skipRateOfRows, skipRateOfColumns))

        for row in range(0, skipRateOfRows):
            for col in range(0, skipRateOfColumns):
                resImg[row, col] = img[row * factor, col * factor]

        return resImg

    def contrastStretching(self, smin=0, smax=255):
        rows, cols, img = self.getImageDetails()

        arr2D = np.array(img)
        rmin = np.amin(arr2D)
        rmax = np.amax(arr2D)

        resImg = np.zeros((rows, cols))
        for row in range(0, rows):
            for col in range(0, cols):
                r = img[row][col]
                resImg[row, col] = (smax - smin) // (rmax - rmin) * (r - rmin + smin)

        return resImg

    def thresholding(self, threshhold):
        rows, cols, img = self.getImageDetails()
        resImg = np.zeros((rows, cols))
        for row in range(0, rows):
            for col in range(0, cols):
                resImg[row, col] = 0 if (img[row, col] < threshhold) else 255

        return resImg

    def logTransformation(self, c=0):
        rows, cols, img = self.getImageDetails()
        c = 255 // np.log(1 + np.amax(img)) if (c == 0) else c
        resImg = np.zeros((rows, cols))
        for row in range(0, rows):
            for col in range(0, cols):
                s = np.log(img[row][col] + 1)
                resImg[row][col] = c * s

        return resImg

    def inverseLogTransformation(self, c=0):
        rows, cols, img = self.getImageDetails()
        c = 255 // np.log(1 + np.amax(img)) if (c == 0) else c
        resImg = np.zeros((rows, cols))
        for row in range(0, rows):
            for col in range(0, cols):
                s = np.exp(img[row][col]) ** (1 / c) - 1
                resImg[row][col] = s

        return resImg

    def powerLawTransformation(self, gamma, c=0):
        rows, cols, img = self.getImageDetails()
        c = 255 // np.log(1 + np.amax(img)) if (c == 0) else c
        resImg = np.zeros((rows, cols))
        for row in range(0, rows):
            for col in range(0, cols):
                s = c * np.power(img[row][col], gamma)
                resImg[row][col] = s

        return resImg

    def grayLevelSlice(self, min, max, newVal=255, keep=False):
        rows, cols, img = self.getImageDetails()
        resImg = np.zeros((rows, cols))
        for row in range(0, rows):
            for col in range(0, cols):
                r = img[row][col]
                if (min >= r and r <= max):
                    resImg[row][col] = newVal
                else:
                    resImg[row][col] = img[row][col] if (keep == True) else 0

        return resImg

    def bitPlaneSlicing(self , picIndex):
        rows, cols, img = self.getImageDetails()
        resImages = []
        for i in range(0, 8):
            temp = np.zeros((rows, cols))
            temp = (img >> i) & 1
            resImages.append(temp);

       
        return resImages[picIndex]


    def Add(self , pixelVal):
        rows, cols, img = self.getImageDetails()
        resImg = np.copy(img)
 
        for row in range(0, rows):
            for col in range(0, cols):
               resImg[row][col] = resImg[row][col] + pixelVal
     
        return resImg
      
    def Diff(self , pixelVal):
     
        rows, cols, img = self.getImageDetails()
        resImg = np.copy(img)
        for row in range(0, rows):
            for col in range(0, cols):
                resImg[row][col] = img[row][col] - pixelVal
           
        return resImg
    def And(self , otherImage):
        rows, cols, img = self.getImageDetails()
        return np.logical_and(img ,otherImage)
    def Or(self , otherImage):
        rows, cols, img = self.getImageDetails()
        return np.logical_or(img ,otherImage)


# %%
