# %%
import numpy as np
from skimage.io import imread 
from matplotlib import pyplot as plt 
from pointProcessing import PointProcessing
from Filters import Filters
class ImageProcessing :
    def __init__(self,imgPath):
        self.img = self.rgb2Gray(imread(imgPath));
        self.imgPath = imgPath
        self.imgState = np.array([])
        x , y = self.img.shape
        self.imgX = x
        self.imgY = y
        self.pointProcessing = PointProcessing(self.img)
        self.filters = Filters(self.img)                                                                                                                                                                            

    def getImageDetails(self):
        return [self.imgX , self.imgY , self.img]     
        

    @staticmethod
    def rgb2Gray (img):
        
        if(len(img.shape) == 2):
            return img
        rows , cols , d = img.shape

        resImg = np.zeros((rows , cols)) 

        for row in range (0 , rows):
            for col in range (0 , cols):
                r,g,b = img[row][col]
                condensedCellVal = (((max(r,g,b) + min(r,g,b)) % 255) // 2)
                resImg[row][col] = condensedCellVal
        

        return resImg

    def adjustIntensityLevel(self , k = 1):
        res = self.pointProcessing.grayIntensity(k)
        self.__update(res)
        return self;
    
    def subSample(self , factor):
        res = self.pointProcessing.Sample(factor)
        self.__update(res)
        return self;
    def contrastStretching(self , smin = 0 , smax = 255):
        res = self.pointProcessing.contrastStretching(smin , smax)
        self.__update(res)
        return self;
    def threshold(self , threshhold):
        res = self.pointProcessing.thresholding(threshhold)
        self.__update(res)
        return self;
    def grayLevelSlicing(self , min , max ,newVal = 255 , keep = False):
        res = self.pointProcessing.grayLevelSlice(min , max , newVal, keep)
        self.__update(res)
        return self;
    def logTransform(self , c = 0):
            res = self.pointProcessing.logTransformation(c)
            self.__update(res)
            return self;
    def inverseLogTransform(self , c = 0):
        res = self.pointProcessing.inverseLogTransformation(c)
        self.__update(res)
        return self;
    def powerLawTransform(self, gamma , c = 0):
        res = self.pointProcessing.inverseLogTransformation(gamma, c)
        self.__update(res)
        return self;


    def minmaxFilter(self,mode):
        res = self.filters.minmaxFilter(mode)
        self.__update(res)
        return self
    def medianFilter(self):
        res = self.filters.medianFilter()
        self.__update(res)
        return self
    def averageFilter(self,sigma=None):
        res = self.filters.averageFilter(sigma)
        self.__update(res)
        return self

    def lablacianFilter(self , neighbors  , sign , composite = False):
        res = self.filters.laplacianFilter(neighbors , sign , composite)
        self.__update(res)
        return self
    def get(self):
        return self.img
    def __update(self,currentImg):
        self.img = currentImg
        self.pointProcessing = PointProcessing(self.img)
        self.filters = Filters(self.img)

    def resetChanges(self):
        self.__update(self.rgb2Gray(imread(self.imgPath)))


    




imgObj = ImageProcessing('./images/grayImage.png')





plt.figure()
plt.subplot(111)
plt.imshow(imgObj.averageFilter(1).get(), cmap='gray')








# %%
