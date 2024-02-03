import cv2
import time
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from jetsonrobotwebcontroller.camera import webcam

def app(request):
    context = {}
    return render(request, "main.html", context)

# Streaming with Motion JPEG tactics
def transmission(camera):
    while True:
        frame = camera.get_frame()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        name = "frame%s.jpg"%timestr
        cv2.imwrite(name, frame[1])
        #print("Filetype frame: ", type(frame[1]))
        yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n')
            
def webcam_feed(request):
    return StreamingHttpResponse(transmission(webcam()), content_type='multipart/x-mixed-replace; boundary=frame')
