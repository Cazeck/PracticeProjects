import cv2, time

first_frame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # To remove noise from the video capture
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    # Delta frame will be a new image
    # Calculating the difference between the first frame and the current frame
    delta_frame = cv2.absdiff(first_frame, gray)

    # If values that are more than 30 difference,
    # We will classify it as white pixel = movement
    # Else black pixel = no movement
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_delta, None, iterations=2)

    (contours,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    print(gray)

    # When q is pressed, break
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()