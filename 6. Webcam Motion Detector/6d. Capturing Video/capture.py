import cv2, time

video = cv2.VideoCapture(0)

a = 1           # Using this as a iteration counter

while True:
    a = a+1
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1)

    # When q is pressed, break
    if key == ord('q'):
        break

print(a)

video.release()
cv2.destroyAllWindows()