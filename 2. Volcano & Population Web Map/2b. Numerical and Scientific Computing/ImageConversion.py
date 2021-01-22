import numpy
import cv2

# Read image file 0 is grayscale, 1 is rgb (color)
im_g = cv2.imread("smallgray.png", 0)

#print(im_g)

# Create image from info from numpy array
cv2.imwrite("newsmallgray.png", im_g)

# Slice data (normal array methods/indexing)
#print(im_g[0:2, 2:4])

# For iterating by columns use .T (transpose) method
#for i in im_g:
#    print(i)

# One by one output
#for i in im_g.flat:
#    print(i)

# Stack three numpy arrays
# #Stack vertically would be vstack instead of hstack
ims = numpy.hstack((im_g, im_g, im_g))
#print(ims)

# Split array into smaller
lst = numpy.vsplit(ims, 3)

print(lst)

#make new bigger image
cv2.imwrite("newmedgray.png", ims)

