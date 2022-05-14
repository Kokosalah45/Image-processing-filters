filter equation in general

send the image and the filter dimensions
get the original dimensions of the image x , y
get the padding levels that will be applied on an image
by sent filter x dimension value ) // 2 (Px)
by sent filter y dimension value ) // 2 (Py)
X = x + (Px)
Y = y + (Py)
the new 2d array dimensions will be X , Y
embed the values of the original into the new one starting at (0 + (Px) , 0 + (Py))
iterating at (i + (Px) , i + (Py))
