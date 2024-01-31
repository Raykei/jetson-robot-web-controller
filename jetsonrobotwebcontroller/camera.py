import cv2

class webcam(object):
    # Is called when an object is created
    def __init__(self):
        rtsp_url = 0 
        self.video = cv2.VideoCapture(rtsp_url)
        # self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        # self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        if not self.video.isOpened():
            print("Cannot open camera")
            exit()
        
    # Is called when an object is about to be destroyed
    def __del__(self):
        self.video.release()    
    
    def get_frame(self):
        # Capture frame-by-frame
        frameReadSucess, frame = self.video.read()

        # if frame is read correctly ret is True
        if not frameReadSucess:
            print("Can't receive frame (stream ended?).")
        # Transform frame to JPEG
        encodeSuccess, jpg = cv2.imencode('.jpg', frame)
        if not encodeSuccess:
            print("Cannot encode to JPG")
        return jpg.tobytes()
