import cv2
video = cv2.VideoCapture(1)
fps = video.get(cv2.CAP_PROP_FPS)
print("CAMERA FPS: ", format(fps))
