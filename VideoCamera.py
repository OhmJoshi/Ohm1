import datetime
import time
timeis = time.strftime("%Y%m%d-%H%M%S")
filename = timeis + ".mp4"
# organize imports
import numpy as np
import cv2

  
# This will return video from the first webcam on your computer.
cap = cv2.VideoCapture(0)  
  
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
  
# loop runs if capturing has been initialized. 
while(True):
    # reads frames from a camera 
    # ret checks return at each frame
    ret, frame = cap.read() 


  
    # Converts to HSV color space, OCV reads colors as BGR
    # frame is converted to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if ret:
        # describe the type of
        # font you want to display
        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
 
        # Get date and time and
        # save it inside a variable
        dt = str(datetime.datetime.now())
 
        # put the dt variable over the
        # video frame
        frame = cv2.putText(frame, dt,
                            (10, 100),
                            font, 1,
                            (210, 155, 155),
                            4, cv2.LINE_8)
         
        # show the video
        cv2.imshow('frame', frame)

      
    # output the frame
    out.write(frame) 
      
    # The original input frame is shown in the window 
    cv2.imshow('Original', frame)
  

  
      
    # Wait for 'a' key to stop the program 
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# De-allocate any associated memory usage 
cv2.destroyAllWindows()