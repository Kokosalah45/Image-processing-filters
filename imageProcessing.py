# %%
import numpy as np
from skimage.io import imread
from matplotlib import pyplot as plt
from pointProcessing import PointProcessing
from Filters import Filters


class ImageProcessing:
    def __init__(self, imgPath):
        self.img = self.rgb2Gray(imread(imgPath));
        x, y = self.img.shape
        self.imgX = x
        self.imgY = y
        self.pointProcessing = PointProcessing(self.img)
        self.filters = Filters(self.img)

    def getImageDetails(self):
        return [self.imgX, self.imgY, self.img]

    @staticmethod
    def rgb2Gray(img):

        if (len(img.shape) == 2):
            return img
        rows, cols, d = img.shape

        resImg = np.zeros((rows, cols))

        for row in range(0, rows):
            for col in range(0, cols):
                r, g, b = img[row][col]
                condensedCellVal = (((max(r, g, b) + min(r, g, b)) % 255) // 2)
                resImg[row][col] = condensedCellVal

        return resImg

    def adjustIntensityLevel(self, k=1):
        res = self.pointProcessing.grayIntensity(k)
        self.__update(res)
        return res;

    def logTransform(self, c=0):
        res = self.pointProcessing.logTransformation(c)
        self.__update(res)
        return res;

    def inverseLogTransform(self, c=0):
        res = self.pointProcessing.inverseLogTransformation(c)
        self.__update(res)
        return res;

    def display_histogram(self):
        img = self.img  # get image reference
        colors_frequency = {}  # initialize dictionary to count frequency of each color

        for x in range(len(img)):
            for y in range(len(img[0])):
                if not colors_frequency.get(img[x][y]):
                    colors_frequency[img[x][y]] = 0
                    continue
                colors_frequency[img[x][y]] = colors_frequency.get(img[x][y]) + 1  # count color frequency

        x_axis = list(colors_frequency)  # get list of colors for X axis
        y_axis = list(colors_frequency)  # get list of frequencies for Y axis

        # Plot the histogram
        plt.figure()
        plt.bar(range(len(colors_frequency)), y_axis, tick_label=x_axis)
        plt.show()

    def __update(self, currentImg):
        self.img = currentImg
        self.imgX, self.imgY = currentImg.shape
        self.pointProcessing = PointProcessing(self.img)
        self.filters = Filters(self.img)


imgObj = ImageProcessing('./images/grayImage.png')
imgObj.display_histogram()
res = imgObj.logTransform()
plt.figure()
plt.subplot(1, 1, 1)
plt.imshow(res, cmap='gray')
res = imgObj.inverseLogTransform()

plt.figure()
plt.subplot(1, 1, 1)
plt.imshow(res, cmap='gray')

# %%
