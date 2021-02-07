import cv2
import glob

# List containing all image file paths
images = glob.glob("sample_images/*.jpg")

# Read each image, resize, display,
# then when window is closed, write the resized image
for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("Hey", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + image.split("\\")[1], re)
