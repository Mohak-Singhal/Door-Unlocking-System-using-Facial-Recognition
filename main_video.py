import cv2
import pygame
import os
import datetime
from simple_facerec import SimpleFacerec
from send_email import send_email

# Initialize Pygame mixer for sound
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound("alarm.wav")

# Initialize face recognition
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(1)

# Create the images_email folder if it doesn't exist
if not os.path.exists("images_email"):
    os.makedirs("images_email")

while True:
    ret, frame = cap.read()
    frame_copy = frame.copy()  # Create a copy of the frame

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame_copy, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame_copy, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame_copy)

    # Capture image and send email if an intruder is detected
    if "Unknown" in face_names:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        image_name = f"intruder_{timestamp}.jpg"
        image_path = os.path.join("images_email", image_name)
        cv2.imwrite(image_path, frame_copy)
        print("Intruder detected! Image captured.")
        send_email(image_path)
        alarm_sound.play()  # Trigger the alarm

    key = cv2.waitKey(1)
    if key == 27:  # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()
