import cv2

print("searching cameras")
for index in range(10):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Camera found at index {index}")
        cap.release()
    else:
        print(f"No camera found at index {index}")