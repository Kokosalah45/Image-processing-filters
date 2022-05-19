
# %%
from cProfile import label
from logging import Filter
from matplotlib import pyplot as plt
import numpy as np

class Filters :
    def __init__(self , img , filterX = 10 , filterY = 10) :
        self.img = img;
        x , y = img.shape
        self.imgX = x
        self.imgY =  y
        self.filterX = filterX 
        self.filterY = filterY 
        self.paddedImage = self.padImage();

    def convolute (self,startX, startY, arr , filter ,mode , sigma=None):
     # 3wd fe eli a5dt meno adek et8abet tany ma7na lesa aylen xDD
     temp = np.array(arr[startX:self.filterX + startX, startY:self.filterY + startY])
     filterCopy = filter.flatten()
     temp = temp.flatten()
     res = np.dot(temp,filterCopy) 
     if(mode == 'average'):
        sumOfProducts = np.sum(res) 
        if(sigma == None):
          return sumOfProducts / (self.filterX * self.filterY)
        return sumOfProducts 

     elif(mode=='laplacian'):
         res *= -1
         pixelVal = np.sum(res)
         return pixelVal 
     elif(mode == 'min'):
              pixelVal = np.amin(res)
              return pixelVal
     elif(mode == 'max'):
              pixelVal = np.amax(res)
              return pixelVal
     elif(mode == 'median'):
              sortedRes = np.copy(res)
              pixelVal = np.median(sortedRes)
              return pixelVal
             


            
   
   
    def padImage(self):
   
        pX = self.filterX // 2
        pY = self.filterY // 2
        X = self.imgX + pX * 2 
        Y = self.imgY + pY * 2
        temp = np.zeros((X , Y))
        for i in range (0 , self.imgX):
            for j in range (0 , self.imgY):
                temp[i + pX][j + pY] = self.img[i][j]
       
        
        return temp

    def updateFilterSize(self,x,y):
        self.filterX = x
        self.filterY = y
        self.paddedImage = self.padImage()
     


    def laplacianFilter(self , neighbors  , sign , composite = False):
        filter = []
        pX = self.filterX // 2 
        pY = self.filterY // 2 
        if(neighbors == 4 ):
             filter = np.zeros((self.filterX,self.filterY))
             filter[1,0] = filter[1,2] = filter[0,1] = filter[2,1] = 1 * sign
             filter[1,1] = (4 + bool(composite)) * -sign
        if(neighbors == 8 ):
             filter = np.ones((self.filterX,self.filterY)) * sign
             filter[1,1] = (8 + bool(composite)) * -sign

        outImage = np.zeros((self.imgX , self.imgY))
        outImage = np.copy(self.paddedImage)
       
        # 3wd fe eli a5dt meno bala4 8abawa bala4 8abawa
        for x in range(pX , self.imgX + pX):
            for y in range(pY , self.imgY + pY):
               outImage[x][y] = self.convolute(x - pX , y - pY , self.paddedImage , filter  , 'laplacian' , None)
        if(composite):
            return outImage
        
        return self.paddedImage + (outImage * sign)
       
      


    def averageFilter(self , sigma = None):
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
                    filter[x][y] = x1 * x2
        ########################
        outImage = np.copy(self.paddedImage)
       
        # 3wd fe eli a5dt meno bala4 8abawa bala4 8abawa
        for x in range(pX , self.imgX + pX):
            for y in range(pY , self.imgY + pY):
               outImage[x][y] = self.convolute(x - pX , y - pY , self.paddedImage , filter , 'average' , sigma)
       
        return outImage 

    def minmaxFilter(self , mode):
        filter = []
        pX = self.filterX // 2 
        pY = self.filterY // 2 
        # 2 - creation filter
        filter = np.ones((self.filterX,self.filterY))
       
        ########################
        outImage = np.copy(self.paddedImage)
       
        # 3wd fe eli a5dt meno bala4 8abawa bala4 8abawa
        for x in range(pX , self.imgX + pX):
            for y in range(pY , self.imgY + pY):
               outImage[x][y] = self.convolute(x - pX , y - pY , self.paddedImage , filter , mode , None)
       
        return outImage 

    def medianFilter(self):
        filter = []
        pX = self.filterX // 2 
        pY = self.filterY // 2 
        # 2 - creation filter
        filter = np.ones((self.filterX,self.filterY))
       
        ########################
        outImage = np.copy(self.paddedImage)
       
        # 3wd fe eli a5dt meno bala4 8abawa bala4 8abawa
        for x in range(pX , self.imgX + pX):
            for y in range(pY , self.imgY + pY):
               outImage[x][y] = self.convolute(x - pX , y - pY , self.paddedImage , filter , 'median' , None)
       
        return outImage 

    def ILPF(self):
        image = self.img


        M = self.imgX
        N = self.imgY

        FT_img = np.fft.fft2(image)
        D0 = 30

        u = np.arange(0, M)
        idx = np.argwhere(u>M/2)
        u[idx] = u[idx]-M

        v = np.arange(0, N)
        idy = np.argwhere(v>N/2)
        v[idy] = v[idy]-N

        V, U = np.meshgrid(v, u)

        D = np.sqrt(U**2 + V**2)

        H = (D <= D0)

        outImage = np.fft.ifft2(FT_img * H)
        return outImage.real

    def IHPF(self):
        image = self.img
        M = self.imgX
        N = self.imgY
        

        FT_img = np.fft.fft2(image)
        D0 = 30

        u = np.arange(0, M)
        idx = np.argwhere(u>M/2)
        u[idx] = u[idx]-M

        v = np.arange(0, N)
        idy = np.argwhere(v>N/2)
        v[idy] = v[idy]-N

        V, U = np.meshgrid(v, u)

        D = np.sqrt(U**2 + V**2)

        H = (D > D0)

        outImage = np.fft.ifft2(FT_img * H)
        return outImage.real

    def BLPF(self):
        image = self.img
        M = self.imgX
        N = self.imgY
        

        FT_img = np.fft.fft2(image)
        D0 = 15
        n = 15

        u = np.arange(0, M)
        idx = np.argwhere(u>M/2)
        u[idx] = u[idx]-M

        v = np.arange(0, N)
        idy = np.argwhere(v>N/2)
        v[idy] = v[idy]-N

        V, U = np.meshgrid(v, u)

        D = np.sqrt(U**2 + V**2)

        H = 1/ ((1+(D0/D)**n) +  1)

        outImage = np.fft.ifft2(FT_img * H)
        return outImage.real

    def BHPF(self):
        image = self.img
        M = self.imgX
        N = self.imgY
        

        FT_img = np.fft.fft2(image)
        D0 = 15
        n = 15

        u = np.arange(0, M)
        idx = np.argwhere(u>M/2)
        u[idx] = u[idx]-M

        v = np.arange(0, N)
        idy = np.argwhere(v>N/2)
        v[idy] = v[idy]-N

        V, U = np.meshgrid(v, u)

        D = np.sqrt(U**2 + V**2)

        H = 1/ ((1+(D0/D)**n) +  1)

        outImage = np.fft.ifft2(FT_img * H)
        return outImage.real
    def GLPF(self):
        image = self.img
        M = self.imgX
        N = self.imgY
        
        FT_img = np.fft.fft2(image)
        D0 = 30
        D0 = (D0**2)*2
        u = np.arange(0, M)
        idx = np.argwhere(u>M/2)
        u[idx] = u[idx]-M

        v = np.arange(0, N)
        idy = np.argwhere(v>N/2)
        v[idy] = v[idy]-N

        V, U = np.meshgrid(v, u)

        D = np.sqrt(U**2 + V**2)
        D = -D**2

        H = np.exp(D/D0)
        outImage = np.fft.ifft2(FT_img * H)
        return outImage.real
    def GHPF(self):
        image = self.img
        M = self.imgX
        N = self.imgY
        
        FT_img = np.fft.fft2(image)
        D0 = 30
        D0 = (D0**2)*2
        u = np.arange(0, M)
        idx = np.argwhere(u>M/2)
        u[idx] = u[idx]-M

        v = np.arange(0, N)
        idy = np.argwhere(v>N/2)
        v[idy] = v[idy]-N

        V, U = np.meshgrid(v, u)

        D = np.sqrt(U**2 + V**2)
        D = -D**2

        H = 1-np.exp(D/D0)
        outImage = np.fft.ifft2(FT_img * H)
        return outImage.real














# %%
