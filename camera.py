# tomasz.bialoblocki

# cv2 library import
import cv2
import os.path

# 1. Creating a video object and set the resolution
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1536)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 2048)

# 2. Variables
a = 0
save_path =  'C:\TEMP'
completeName = os.path.join(save_path, "camera_capture.jpg")

# 3. Loop
while True:
    a = a + 1
   
    # 4. Create a frame object
    check, frame = video.read()

    # You can do it in gray
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 5. Show the frame
    cv2.imshow("Capturing",frame)
   
    # 6. You can do it by keypress
    #key = cv2.waitKey(1)
    #if key == ord('q'):
    break

# 7. Image saving
showPic = cv2.imwrite(completeName,frame)
print(showPic)

# 8. Shutdown the camera
video.release()
cv2.destroyAllWindows 
