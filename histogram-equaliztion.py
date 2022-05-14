# %%
from itertools import accumulate
from time import time
import numpy as np
import math
from matplotlib import pyplot as plt 
from skimage.io import imread 
from imageProcessing import ImageProcessing

img = imread('./images/grayImage.png')
imgGrayed = ImageProcessing.rgb2Gray(img)
rows, cols = imgGrayed.shape

arr2D = np.array(imgGrayed)
grayLevelValueThreshold = (2 ** math.ceil(math.log(np.amax(arr2D) , 2))) - 1 

map1 = {}
rows, cols = arr2D.shape

mappingMedium = grayLevelValueThreshold / (rows * cols);
for scale in range(0,grayLevelValueThreshold + 1):
    map1.setdefault(scale , 0 )


for row in range(0,rows):
    for col in range(0,cols):
        map1[arr2D[row,col]] = map1[arr2D[row,col]] + 1
print("occurences : " , map1)


arr2= np.array(list(map1.values()))

accumulatedArray = np.cumsum(arr2)


for i in range(0,len(map1)):
    map1[i] = accumulatedArray[i]

print("accumulation : " , map1)



for i in range(0,len(map1)):
    map1[i] = math.ceil(map1[i] * mappingMedium)

print("new gray value : " , map1)




for row in range(0,rows):
    for col in range(0,cols):
        arr2D[row,col] = map1[arr2D[row,col]] 






plt.figure()
plt.subplot(1,1,1)
plt.imshow(img , cmap='gray')
plt.clf()
plt.subplot(1,1,1)
plt.imshow(arr2D, cmap='gray')



















# %%
