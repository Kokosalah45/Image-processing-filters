
from matplotlib import pyplot as plt
import numpy as np

class Filters :
    def __init__(self , img , filterX = 3 , filterY = 3) :
        self.img = img;
        x , y = img.shape
        self.imgX = x
        self.imgY =  y
        self.filterX = filterX 
        self.filterY = filterY 
        self.paddedImage = None;

    def convolute (self,startX, startY, arr , filter , sigma=None):
     # 3wd fe eli a5dt meno adek et8abet tany ma7na lesa aylen xDD
     temp = np.array(arr[startX:self.filterX + startX, startY:self.filterY + startY])
     filterCopy = filter.flatten()
     temp = temp.flatten()
     res = np.dot(temp,filterCopy)
     sumOfProducts = np.sum(res) 
     if(sigma == None):
         return sumOfProducts // (self.filterX * self.filterY)
    
     return sumOfProducts ;
   
    def padImage(self):
        if( self.paddedImage != None ):
            return
        pX = self.filterX // 2 
        pY = self.filterY // 2 
        X = self.imgX + pX * 2
        Y = self.imgY + pX * 2
        temp = np.zeros((X , Y))
        for i in range (0 , self.imgX):
            for j in range (0 , self.imgY):
                temp[i + pX][j + pY] = self.img[i][j]
        
        self.paddedImage = temp

    def averageFilter(self , sigma = None):
        # 1 - padding
        self.padImage()
        filter = []
        pX = self.filterX // 2 
        pY = self.filterY // 2 
        # 2 - creation filter
        if (sigma == None):
            filter = np.ones((self.filterX,self.filterY))
        else:
            filter = np.zeros((self.filterX,self.filterY))
            for x in range(-pX,pX + 1):
                for y in range(-pY,pY + 1) :
                    x1 =  1 / (2 * np.pi * ( sigma ** 2))
                    x2 = np.exp(  -(x**2+y**2)   /  (2 * (sigma ** 2)) )
                    filter[x + pX ][y + pY] = x1 * x2
        ########################
        outImage = np.zeros((self.imgX , self.imgY))
        outImage = self.paddedImage
       
        # 3wd fe eli a5dt meno bala4 8abawa bala4 8abawa
        for x in range(pX , self.imgX + pX):
            for y in range(pY , self.imgY + pY):
               outImage[x][y] = self.convolute(x - pX , y - pY , self.paddedImage , filter , sigma)
       
                
               
        
        return outImage 


 













# %%
