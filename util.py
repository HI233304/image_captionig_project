import cv2

def capture_image_from_camera(file_name="camera_capture.jpg"):
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        cv2.imwrite(file_name, image)
    cam.release()
    return file_name