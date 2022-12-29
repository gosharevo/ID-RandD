import cv2

face_cascade = cv2.CascadeClassifier('bot/haarcascades/haarcascade_frontalface_default.xml')


async def photo_faces(image_path: str) -> bool:
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return len(faces) > 0
