import cv2

# Load our input image
image = cv2.imread('./images/input.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

# We use cvtColor, to convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(3)
cv2.destroyAllWindows()

# printing out the dimensions of the image
# entering an array and it contains a tuple
# Two dimensions of height and widths
# the third column represent the rgb values of the image

print(image.shape)

# saving images 

#cv2.imwrite('output.jpg', image)
#cv2.imwrite('output.png', image)
cv2.imwrite('gray.jpg', gray_image)

