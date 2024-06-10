import cv2
import os


cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Unable to read camera ... !")

outputDir = "output_images"
os.makedirs(outputDir, exist_ok=True)

imageCount = 94

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Webcam", frame)

    k = cv2.waitKey(1)

    if k%256 == 27: # press 'esc' to save the frame ... 
        print("Escape hit, closing ... !")
        break
    elif k%256 == ord('s'): # press 's' to save the frame ... 
        imageName = os.path.join(outputDir, "opencv_frame_{}.png".format(imageCount))
        cv2.imwrite(imageName, frame)
        print("{} written ... !".format(imageName))
        imageCount +=1

cap.release()
cv2.destroyAllWindows()