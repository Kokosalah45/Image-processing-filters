# %%
from re import S
from tkinter import Image
from imageio import read
import numpy as np
from matplotlib import pyplot as plt 
from skimage.io import imread 

#x = np.shape([[1,2],[3,4] ])

class PointProcessing :
      def __init__(self,img):
        self.img = img;
        x , y = img.shape
        self.imgX = x
        self.imgY =  y

      def getImageDetails(self) :
          return [self.imgX , self.imgY , self.img]     



      def grayIntensity(self , k = 1) :
        rows , cols  , img = self.getImageDetails() 
        resImg = np.zeros((rows, cols)) 
        for row in range (0 , rows):
          for col in range (0 , cols):
            l = (2**k) - 1
            resImg[row][col] = img[row][col] % l
        return resImg

      def Sample (self, factor) :
        rows , cols , img = self.getImageDetails()
        skipRateOfRows = rows // factor
        skipRateOfColumns = cols // factor
    
        resImg =  np.zeros((skipRateOfRows, skipRateOfColumns ))

        for row in range (0 , skipRateOfRows):
            for col in range (0 , skipRateOfColumns):
             resImg[row,col] = img[row*factor , col * factor]

        return resImg
      
      def contrastStretching(self, smin = 0 , smax = 255):
        rows , cols  , img = self.getImageDetails()

        arr2D = np.array(img)
        rmin = np.amin(arr2D)
        rmax = np.amax(arr2D)  
      
        resImg = np.zeros((rows , cols))
        for row in range (0 , rows):
          for col in range (0 , cols): 
             r = img[row][col]
             resImg[row,col] =  (smax - smin) // (rmax - rmin) * (r - rmin + smin)

        return resImg

      def logTransformation (self , c = 0):
        rows , cols , img = self.getImageDetails()
        c =  255 // np.log( 1 + np.amax(img) ) if(c==0) else c
        resImg = np.zeros((rows , cols))
        for row in range (0 , rows):
          for col in range (0 , cols):
             s=np.log(img[row][col] + 1)
             resImg[row][col] =  c * s
        
        return resImg   
      def inverseLogTransformation (self , c = 0):
        rows , cols , img = self.getImageDetails()
        c =  255 // np.log( 1 + np.amax(img) ) if(c==0) else c
        resImg = np.zeros((rows , cols))
        for row in range (0 , rows):
          for col in range (0 , cols):
             s=np.exp(img[row][col]) ** (1/c) - 1
             resImg[row][col] =  s
        
        return resImg   
      def powerLawTransformation (self , gamma, c = 0 ):
        rows , cols , img = self.getImageDetails()
        c =  255 // np.log( 1 + np.amax(img) ) if(c==0) else c
        resImg = np.zeros((rows , cols))
        for row in range (0 , rows):
          for col in range (0 , cols):
             s= c * np.power(img[row][col] , gamma) 
             resImg[row][col] =  s
        
        return resImg   
   


     
      def thresholding(self , threshhold):
        rows,cols,img = self.getImageDetails()
        resImg = np.zeros((rows , cols))
        for row in range (0 , rows):
          for col in range (0 , cols): 
             resImg[row,col] = 0 if (img[row,col] < threshhold) else 255

        return resImg









#################################################

imgObj = PointProcessing(imread('./images/grayImage.png'))
res = imgObj.powerLawTransformation(1)
plt.figure()
plt.subplot(1,1,1)
plt.imshow(res , cmap="gray")
res = imgObj.powerLawTransformation(0.5)

plt.figure()
plt.subplot(1,1,1)
plt.imshow(res , cmap="gray")

res = imgObj.powerLawTransformation(0.2)

plt.figure()
plt.subplot(1,1,1)
plt.imshow(res , cmap="gray")


res = imgObj.powerLawTransformation(2)

plt.figure()
plt.subplot(1,1,1)
plt.imshow(res , cmap="gray")





# %%
