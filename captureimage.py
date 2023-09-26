import cv2
import time

# Define the folder where you want to save the images
folder = "/Users/yashas.m/Downloads/Smart-Attendance-System-main/image "
name=str(input("enter the name\t"))

# Create a VideoCapture object to capture from the webcam
cap = cv2.VideoCapture(0)

# Start capturing images
while True:
    # Capture the current frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("image capturing", frame)

    # Press `q` to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        # Save the frame to the folder
        cv2.imwrite(f"{folder}/{name}.jpg", frame)
        # Break out of the loop
        break

# Release the VideoCapture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
