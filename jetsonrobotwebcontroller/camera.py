import cv2
import threading

global openCount
openCount = 0

class webcam(object):
    # Is called when an object is created
    def __init__(self):
        global cameraOpen
        self.video = cv2.VideoCapture(0)
        # self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        # self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        if not self.video.isOpened():
            print("No se puede abrir la camara, revisar conexión USB")
            exit()
        else:
            print("La camara se abrió correctamente")
            cameraOpen =+ 1
    # Is called when an object is about to be destroyed
    # def __del__(self):
    #     self.video.release()    
    
    def get_frame(self):
  
        # Capture frame-by-frame
        frameReadSucess, frame = self.video.read()

        # if frame is read correctly ret is True
        if not frameReadSucess:
            print("No se pudo leer el frame (stream ended?).")
         
        # Transform frame to JPEG
        encodeSuccess, jpg = cv2.imencode('.jpg', frame)
        #print("FRAME ENCODEADO")
        if not encodeSuccess:
            print("No se pudo transformar frame a JPG")
        return jpg.tobytes(), frame, cameraOpen
